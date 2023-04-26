###### Implementing recipes api

-   Lets crete the serializer for the recipe model

-   inside the recipe app create a new file called serializers.py

```py
"""Serializers for recipe app"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""

    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
            "description",
        )
        read_only_fields = ("id",)
```

-   lets create the viewset for the recipe model. In views.py iside recipe app

```py
"""Views for recipe api"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for recipe APIs"""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by("-id")
```

-   Create urls.py inside recipe app

```py
"""URL mapping for recipes API"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views


router = DefaultRouter()
router.register("recipes", views.RecipeViewSet)

app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
```

-   In urls.py in app folder

```py
urlpatterns = [
    ...
    path("api/recipe/", include("recipe.urls")),
]
```
