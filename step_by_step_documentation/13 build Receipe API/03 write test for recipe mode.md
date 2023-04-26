###### Write test for recipe mode

-   in test_model.py inside core directory, import Decimal and models

```py
from decimal import Decimal
from core import models
```

-   create test for recipe model

```py
def test_create_recipe(self):
        """Test creating a new recipe"""
        user = get_user_model().objects.create_user(
            "test@example.com", "Testpass123"
        )  # noqa
        recipe = models.Recipe.objects.create(
            user=user,
            title="Example recipe name",
            time_minutes=5,
            price=Decimal("10.50"),
            description="Example recipe description",
        )

        self.assertEqual(str(recipe), recipe.title)
```
