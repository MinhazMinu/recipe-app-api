###### Tests for manage user api

```py
ME_URL = reverse("user:me")
```

-   create a new test method for manage user api

-   Create a PrivateUserApiTests class that inherits from TestCase class

```py
class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        self.user = create_user(
            email="test@example.com",
            password="testpass123",
            name="Test Name",
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(
            res.data, {"name": self.user.name, "email": self.user.email}  # noqa
        )
```

-   POST is not allowed in _ME_URL_

```py
    def test_post_me_not_allowed(self):
        """Test that POST is not allowed on the me url"""
        res = self.client.post(ME_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
```

-   Test Update user profile

```py
def test_update_user_profile(self):
    """Test updating the user profile for authenticated user"""
    payload = {"name": "New Name", "password": "newpass123"}

    res = self.client.patch(ME_URL, payload)

    self.user.refresh_from_db()
    self.assertEqual(self.user.name, payload["name"])
    self.assertTrue(self.user.check_password(payload["password"]))
    self.assertEqual(res.status_code, status.HTTP_200_OK)
```
