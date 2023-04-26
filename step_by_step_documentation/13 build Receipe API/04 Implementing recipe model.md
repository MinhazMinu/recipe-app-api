###### implementing recipe model

-   in models.py import

```py
from django.conf import settings
```

```py
class Recipe(models.Model):
    """Recipe object."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
```

-   Now register the model in admin.py

```py
admin.site.register(models.Recipe)
```

-   Now create migration

```sh
docker-compose run --rm app sh -c "python manage.py makemigrations"
```

-   now Run the test again

```sh
docker-compose run --rm app sh -c "python manage.py test"
```
