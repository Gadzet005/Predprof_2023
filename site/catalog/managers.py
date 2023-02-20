import datetime

from django.db import models
from django.db.models import Q, F

from queries.models import SiteQueryNote


class SiteManager(models.Manager):
    @staticmethod
    def annotate_rating(queryset):
        return (
            queryset
            .prefetch_related('ratings')
            .annotate(
                rating_avg=models.Avg('ratings__rating'),
                rating_num=models.Count('ratings', distinct=True),
                )
            )
    
    @staticmethod
    def annotate_query_notes(queryset):
        return (
            queryset
            .prefetch_related(
                models.Prefetch(
                    'query_notes', 
                    SiteQueryNote.objects.filter(
                        note_time__gte=(datetime.datetime.now() - datetime.timedelta(days=1))
                        )
                    )
                )
            .annotate(avg_ping=models.Avg('query_notes__ping'))
        )

    @staticmethod
    def add(queryset, *functions):
        ''' Метод для использования множества функций на queryset '''

        for func in functions:
            queryset = func(queryset)
        return queryset

    def enabled(self, user):
        if user.is_authenticated:
            queryset = (
                self.get_queryset()
                .filter(Q(user_site__user=user) | Q(is_on_catalog=True))
                )
        else:
            queryset = self.get_queryset().filter(is_on_catalog=True).annotate()

        return self.add(queryset, self.annotate_rating, self.annotate_query_notes)

    def get_for_main_catalog(self):
        base_queryset = (
            self.get_queryset()
            .filter(is_on_catalog=True)
            .order_by(F('rating_num') * F('rating_avg')).reverse()
        )
        return self.add(base_queryset, self.annotate_rating, self.annotate_query_notes)

    def get_user_sites(self, user):
        base_queryset = self.get_queryset().filter(user_site__user=user).order_by('-id')
        return self.add(base_queryset, self.annotate_query_notes)
