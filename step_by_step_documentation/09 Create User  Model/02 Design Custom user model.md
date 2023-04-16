###### Custom User model

-   User Fields
    -   email (EmailFields)
    -   name (CharFields)
    -   is_active (BooleanField)
    -   is_staff (BooleanField)

* User Model Manager
    * Used to manage objects
    * Custom login fro creating objects
        * Hash Password
    * Used by Django CLI
        * Create super user

###### BaseUserManager
* Base class for managing users
* Useful helper methods
    * normalize_emails: for storing emails consistently
* Methods we will define
    * create_user: called when creating user


