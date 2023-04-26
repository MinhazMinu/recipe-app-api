###### implementing manage user api

-   In serializers.py add this code:

```python
def update(self, instance, validated_data):
    """Update a user, setting the password correctly and return it."""
    password = validated_data.pop("password", None)
    user = super().update(instance, validated_data)

    if password:
        user.set_password(password)
        user.save()

    return user
```

Here we create a function that will update the user and set the password correctly.

-   in views.py add this code:

```python
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
```
* Add url in urls.py

```python