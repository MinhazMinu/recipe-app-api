###### Fixing Database Race Condition

> A race condition occurs when two threads access a shared variable at the same time. The first thread reads the variable, and the second thread reads the same value from the variable. Then the first thread and second thread perform their operations on the value, and they race to see which thread can write the value last to the shared variable.
> The value of the thread that writes its value last is preserved, because the thread is writing over the value that the previous thread wrote.

-   Problem with docker compose
    -   Using depends_on ensures service starts
    -   but is dose not ensure application is running

*   Solution
    -   Make custom Django command "wait_for_db"
        -   It check for database availability
        -   Continue when database ready
    -   Create Custom Django management command
