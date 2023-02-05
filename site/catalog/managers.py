from django.db import models
from django.db.models import Q


class SiteManager(models.Manager):
    def enabled(self, user):
        if user.is_authenticated:
            return self.get_queryset().filter(
                Q(user_site__user=user) | Q(is_on_catalog=True)
                )
        return self.get_for_main_catalog()

    def get_for_main_catalog(self):
        return self.get_queryset().filter(is_on_catalog=True)

    def get_user_sites(self, user):
        return self.get_queryset().filter(user_site__user=user)
