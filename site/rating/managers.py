from django.db import models


class RatingManager(models.Manager):
    def get_user_rating(self, site, user):
        if user.is_authenticated:
            return self.get_queryset().filter(site=site, user=user).first()

    def get_site_feedbacks(self, site):
        return (
            self.get_queryset()
            .filter(site=site)
            .exclude(
                models.Q(feedback__isnull=True) | models.Q(feedback__exact='')
                )
            .order_by('creation_date')
            .select_related('user')
            )
