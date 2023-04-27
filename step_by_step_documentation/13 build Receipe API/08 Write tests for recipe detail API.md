###### write tests for recipe detail API

-   create a function for send recipe id as an argument in url

```py
def detail_url(recipe_id):
    """Return recipe detail URL"""
    return reverse('recipe:recipe-detail', args=[recipe_id])
```

-   Now create the test function

```py
def test_get_recipe_detail(self):
    """Test getting recipe detail"""
    recipe = create_recipe(user=self.user)

    url = detail_url(recipe.id)
    res = self.client.get(url)

    serializers = RecipeDetailSerializer(recipe)
    self.assertEqual(res.data, serializers.data)
```
