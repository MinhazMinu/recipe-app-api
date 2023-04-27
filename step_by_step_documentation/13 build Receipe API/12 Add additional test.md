###### Add additional test api

```py
def test_partial_update(self):
        """Test updating a recipe with PATCH"""
        original_link = "http://example.com/recipe.pdf"
        recipe = create_recipe(user=self.user)
        payload = {
            "title": "Updated title",
            "link": original_link,
            "description": "Updated description",
        }
        url = detail_url(recipe.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        recipe.refresh_from_db()
        for k, v in payload.items():
            self.assertEqual(getattr(recipe, k), v)

    def test_full_update(self):
        """Test updating a recipe with PUT"""
        recipe = create_recipe(user=self.user)
        payload = {
            "title": "Updated title",
            "time_minutes": 20,
            "price": Decimal("10.00"),
            "description": "Updated description",
            "link": "http://example.com/recipe.pdf",
        }
        url = detail_url(recipe.id)
        res = self.client.put(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        recipe.refresh_from_db()
        for k, v in payload.items():
            self.assertEqual(getattr(recipe, k), v)
        self.assertEqual(recipe.user, self.user)

    def test_update_user_returns_error(self):
        """Test that updating user returns error"""
        new_user = create_user(
            email="user2@example.com",
            password="testpass123",
        )
        recipe = create_recipe(user=self.user)
        payload = {"user": new_user.id}

        url = detail_url(recipe.id)
        self.client.patch(url, payload)

        recipe.refresh_from_db()

        self.assertEqual(recipe.user, self.user)

    def test_delete_recipe(self):
        """Test deleting a recipe"""
        recipe = create_recipe(user=self.user)
        url = detail_url(recipe.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Recipe.objects.filter(id=recipe.id).exists())

    def test_delete_other_users_recipe_error(self):
        """Test that other user cannot delete recipe"""
        new_user = create_user(
            email="user2@example.com",
            password="testpass123",
        )
        recipe = create_recipe(user=new_user)

        url = detail_url(recipe.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(Recipe.objects.filter(id=recipe.id).exists())
```
