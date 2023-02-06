from django.db import models
from django.db.models import Q


class SiteManager(models.Manager):
    def annotate_rating(self, queryset):
        return (
            queryset
            .prefetch_related('ratings')
            .annotate(
                rating_avg=models.Avg('ratings__rating'),
                rating_num=models.Count('ratings'),
                )
            )

    def enabled(self, user):
        if user.is_authenticated:
            queryset = (
                self.get_queryset()
                .filter(Q(user_site__user=user) | Q(is_on_catalog=True))
                )
        else:
            queryset = self.get_queryset().filter(is_on_catalog=True).annotate()

        return self.annotate_rating(queryset)

    def get_for_main_catalog(self):
        base_queryset = (
            self.get_queryset()
            .filter(is_on_catalog=True)
        )
        return (
            self.annotate_rating(base_queryset)
            .order_by('-rating_num', '-rating_avg', '-id')
            )

    def get_user_sites(self, user):
        return self.get_queryset().filter(user_site__user=user).order_by('-id')
