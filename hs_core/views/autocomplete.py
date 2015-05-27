from django.contrib.auth.models import User, Group

from ga_resources.utils import get_user, json_or_jsonp
from hs_core.models import GenericResource, Party, Contributor, Creator
from hs_core.hydroshare import get_resource_list
from hs_core.hydroshare.utils import get_resource_types

# def get_resource_list(
#         group=None, user=None, owner=None,
#         from_date=None, to_date=None,
#         start=None, count=None,
#         keywords=None, dc=None,
#         full_text_search=None,
#         published=False,
#         edit_permission=False,
#         public=False,
#         types=None
# ):

def autocomplete(request):
    term = request.GET.get('term')
    resp = []

    types = [t for t in get_resource_types() if term.lower() in t.__name__.lower()]
    resp += [{'label': 'type', 'value': t.__name__, 'id': t.__name__} for t in types]

    # Party calculations are expensive and complicated. Deferring to focus on lower hanging fruit
    #
    parties = []
    def get_party_type(party):
        if Contributor.objects.filter(id=party.id).exists():
            return 'Contributor'
        elif Creator.objects.filter(id=party.id).exists():
            return 'Author'
        else:
            return None
    seen = set()
    filter_types = {
        'name': 'name__istartswith',
        'email': 'email__iexact',
    }
    for model in (Creator, Contributor):
        for filter_type in filter_types:
            for party in model.objects.filter(**{filter_types[filter_type]: term}):
                party_type = get_party_type(party)
                if party_type:
                    name = model.__name__
                    if model is Creator:
                        name = "Author"
                    if (name, party.name) not in seen:
                        seen.add((name, party.name))
                        resp.append({
                            'label': name,
                            'type': 'party',
                            'id': getattr(party, filter_type, 'id'),
                            'value': party.name,
                        })

    owners = User.objects.filter(username__istartswith=term)
    for owner in owners:
        if owner.first_name and owner.last_name:
            name = "%s %s (%s)" % (owner.first_name, owner.last_name, owner.username)
        elif owner.first_name:
            name = "%s (%s)" % (owner.first_name, owner.username)
        elif owner.last_name:
            name = "%s (%s)" % (owner.last_name, owner.username)
        else:
            name = owner.username
        resp.append({
            'label': 'Owner',
            'type': 'owner',
            'id': owner.username,
            'value': name,
        })

    # resources = get_resource_list(
    #     full_text_search=term,
    # )

    # todo: users
    # todo: groups
    # todo: other conditions?

    return json_or_jsonp(request, resp)
