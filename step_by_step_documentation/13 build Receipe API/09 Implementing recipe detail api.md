###### Implementing recipe detail api

-   First create the serializer for recipe detail api
-   In serializers.py inside recipe app create a new serializer class

```py
class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail  view"""

    class meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["description"]
```

-   in views.py inside recipe app create a new view class

```py
def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == "list":
            return serializers.RecipeSerializer
        return self.serializer_class

```
