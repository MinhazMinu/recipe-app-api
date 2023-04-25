###### Test case for token api

-   in test_user_api.py file add the following code:

```python
TOKEN_URL = reverse('user:token')
```

-   create a function for test create token for user

```python
def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        user_details = {
            "email": "test@example.com",
            "password": "pw",
            "name": "Test Name",
        }
        create_user(**user_details)
        payload = {
            "email": user_details["email"],
            "password": user_details["password"],
        }  # noqa

        res = self.client.post(TOKEN_URL, payload)

        res.assertIn("token", res.data)
        res.assertEqual(res.status_code, status.HTTP_200_OK)
```

-   to test bad credentials

```python
def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        create_user(email="test@example.com", password="testpass")

        payload = {"email": "test@example.com", "password": "wrong"}
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
```

-   to test balnk password

```python
def test_create_blank_password(self):
        """Test that password is required. Blank password return an error"""
        payload = {
            "email": "test@example.com",
            "password": "",
        }  # noqa

        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
```
