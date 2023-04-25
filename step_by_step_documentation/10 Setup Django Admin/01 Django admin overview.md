###### Django Admin panel

-   How to enable Django Admin
    -   Need to enable per model
    -   Inside admin.py we need to register the model
        -   admin.site.register(Recipe)

*   Customizing

    -   Create class based off ModelAdmin or UserAdmin
    -   Override/set class variables

*   Changing list of objects
    -   ordering: Change ordering ( ascending, descending)
    -   list_display: fields to appear in list
*   Add and update page
    -   fieldsets: control layout of page
    -   readonly_fields: fields that cannot be changed
    -   add_fieldsets: fields displayed only on add page
