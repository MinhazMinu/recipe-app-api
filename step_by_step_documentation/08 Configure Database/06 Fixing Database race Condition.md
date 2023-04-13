###### Fixing Database Race Condition

-   Problem with docker compose
    -   Using depends_on ensures service starts
    -   but is dose not ensure application is running

*   Solution
    -   Make Django "wait for db"
        -   It check for database availability
        -   Continue when database ready
    -   Create Custom Django management command
