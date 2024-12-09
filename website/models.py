from django.db import models
from django.core.validators import MaxValueValidator

class FilmLog(models.Model):
    YES_NO_CHOICES = [
        (True, "Yes"),
        (False, "No"),
    ]
    logged_at = models.DateTimeField(auto_now_add=True)
    film_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    year_of_release = models.PositiveIntegerField(default=1888)
    personal_rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        validators=[MaxValueValidator(5.0)]  # Ensures rating is <= 5
    )
    review = models.TextField(default="No review provided")
    would_recommend = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    I_have_seen_this_film_before = models.BooleanField(default=False)  # Default set to 'No'

    def __str__(self):
        return f"{self.film_title} ({self.year_of_release})"



