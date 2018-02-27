from django.core.management.base import BaseCommand
from hs_core.models import BaseResource
from hs_core.hydroshare.features import Features
from django.contrib.auth.models import Group
from hs_explore.utils import Utils
from datetime import datetime
from pprint import pprint


class Command(BaseCommand):
    help = "Print information about a user."

    def handle(self, *args, **options):
        # x = Features.visited_resources(datetime(2017, 11, 20, 0, 0, 0, 0),
        #                                datetime(2018, 1, 1, 0, 0, 0, 0))
        # pprint(x)
        # x = Features.resource_viewers(datetime(2017, 11, 20, 0, 0, 0, 0),
        #                               datetime(2018, 1, 1, 0, 0, 0, 0))
        # pprint(x)
        # x = Features.resource_owners()
        # pprint(x)
        # x = Features.resource_editors()
        # pprint(x)
        # x = Features.resource_downloads(datetime(2017, 11, 20, 0, 0, 0, 0),
        #                                 datetime(2018, 1, 1, 0, 0, 0, 0))
        # pprint(x)
        # x = Features.user_downloads(datetime(2017, 11, 20, 0, 0, 0, 0),
        #                             datetime(2018, 1, 1, 0, 0, 0, 0))
        # pprint(x)
        # x = Features.resource_apps(datetime(2017, 11, 20, 0, 0, 0, 0),
        #                            datetime(2018, 1, 1, 0, 0, 0, 0))
        # pprint(x)
        # x = Features.user_apps(datetime(2017, 11, 20, 0, 0, 0, 0),
        #                        datetime(2018, 1, 1, 0, 0, 0, 0))
        # pprint(x)
        # print the feature vector for all resources.

        # for r in BaseResource.objects.all():
        #     # pprint(Features.resource_features(r))
        #     Utils.write_dict("ALL_RESOURCES_ALL_FEATURES.OUT", Features.resource_features(r))

        # x = Features.user_my_resources()
        # pprint(x)

        # x = Features.user_favorites()
        # pprint(x)

        # x = Features.user_owned_groups()
        # pprint(x)

        # x = Features.user_edited_groups()
        # pprint(x)

        # x = Features.user_viewed_groups()
        # pprint(x)

        # for g in Group.objects.all(): 
        #     x = Features.resources_viewable_via_group(g)
        #     pprint(g)
        #     pprint(Features.explain_group(g))
        #     pprint(x)

        for g in Group.objects.all(): 
            x = Features.resources_editable_via_group(g)
            pprint(g)
            pprint(Features.explain_group(g))
            pprint(x)