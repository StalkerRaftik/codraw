from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


class Genre(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    class Meta:
        constraints = [UniqueConstraint(fields=['name'], name='unique_genre_name')]


class AnimeStatus(models.TextChoices):
    ANNOUNCED = 'AN', 'Announced'
    ONGOING = 'ON', 'Ongoing'
    RELEASED = 'RE', 'Released'


class Anime(models.Model):
    name = models.CharField(max_length=60, blank=True)
    original_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    premiere_date = models.DateField(blank=True)
    status = models.CharField(
        max_length=2,
        choices=AnimeStatus.choices,
        default=AnimeStatus.ANNOUNCED,
    )
    episodes_count = models.IntegerField(default=-1)  # negative means unknown count
    added_episodes = models.IntegerField(default=0)
    image = models.ImageField('media/anime/images')
    genres = models.ManyToManyField(Genre, related_name='anime')

    # temporary rating from dataset. Will be overwritten after ?? reviews
    raw_rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True)
    # temporary visits from dataset. Will be overwritten after ?? detail page visits
    raw_visits = models.PositiveBigIntegerField(blank=True)

    class Meta:
        constraints = [UniqueConstraint(fields=['original_name'], name='unique_anime_original_name')]


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        constraints = [UniqueConstraint(fields=['owner', 'anime'], name='unique_anime_user')]
