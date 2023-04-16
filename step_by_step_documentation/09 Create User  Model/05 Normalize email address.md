###### Normalize email user

> For email addresses, foo@bar.com and foo@BAR.com are equivalent; the domain part is case-insensitive according to the RFC specs. Normalizing means providing a canonical representation, so that any two equivalent email strings normalize to the same thing.
> Normalize the email address by lowercasing the domain part of it.

###### Adding test case for normalizing email

-   In test*models.py we add another method \_test_new_user_email_normalized*

```py
def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@example.com", "TEST3@example.com"],
            ["test4@example.com", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email, password="Testpass123")
            self.assertEqual(user.email, expected)
```

-   run the test

```sh
docker-compose run --rm app sh -c " python manage.py test'
```

it will fails ( as we do not implement this yet)

###### implement email normalization

we simply need to add self.normalize_email() inside create_user method in models.py

```py
def create_user(self, email, password=None, **extra_fields):
        """Create and save and return a  new user."""
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
```

Now re run the test.
