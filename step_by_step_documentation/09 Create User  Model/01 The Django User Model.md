###### Django Auth

-   Built in Registration, Login, Auth system
-   Integrate with Django Admin

###### Default User model

-   Username instead of email
-   Not easy to customize

###### Customize user model

-   Create model
    -   Base from AbstractBaseUser and PermissionsMixin
-   Create custom manager
    -   Used for CLI integration
-   Set AUTH_USER_MODEL in settings.py
-   Create and run migration

###### AbstractBaseUserClass

-   Provides feature for authentication
-   Dose not include fields

###### PermissionMixin

-   Support for Django permission system
-   Includes fields and methods

###### Common issues

-   Running migration before setting custom model
-   Typos
-   Indentation
