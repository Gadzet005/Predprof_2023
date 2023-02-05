from django.db import models


class RatingManager(models.Manager):
    def get_rating(self, site):
        result = (
            self.get_queryset()
            .filter(site=site)
            .aggregate(
                rating_avg=models.Avg('rating'),
                rating_num=models.Count(),
                )
            )
        if result['rating_avg']:
            result['rating_avg'] = round(result['rating_avg'], 2)
        return result

    def get_user_rating(self, site, user):
        if user.is_authenticated:
            return self.get_queryset().filter(site=site, user=user).first()
