###### Tests for admin panel

-   first crete a test_admin.py in tests directory

```py
""" Test for django admin modification"""

from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test for Django admin site"""
    # set up client and user which will be needed for every test case
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="password123",
            name="Test user",  # noqa
        )

    # test user list
    def test_users_lists(self):
        """Test that users are listed on user page"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
```

-   run the test

```sh
docker-compose run --rm app sh -c "python manage.py test"
```
