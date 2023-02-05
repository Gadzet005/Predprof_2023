from django.db import models

from rating.managers import RatingManager
from catalog.models import Site
from users.models import User


RATING_CHOICES = (
    (1, 'Ужасно...'),
    (2, 'Плохо'),
    (3, 'Сойдёт'),
    (4, 'Нравится'),
    (5, 'Обожаю!'),
)


class SiteRating(models.Model):
    site = models.ForeignKey(Site, verbose_name='сайт', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    rating = models.SmallIntegerField('оценка', choices=RATING_CHOICES)
    feedback = models.TextField('отзыв', max_length=5000, null=True, blank=True)

    objects = RatingManager()

    class Meta:
        default_related_name = 'ratings'
        constraints = (
            models.UniqueConstraint(
                fields=('site', 'user'), name='site_user_unique'
            ),
        )
