###### Mocking

-   Override or change behavior of dependencies
-   Avoid unintended side effects
-   Isolate code being tested

###### Why we use Mocking

-   Avoid relying on external services
    -   Can`t guarantee they will be available
    -   Makes tests unpredictable and inconsistent

*   Avoid unintended consequences
    -   Accidentally sending emails
    -   Overloading external services

###### Example

register_user() ➡ create_in_db() ➡ send_welcome_email()

-   in this case, when we test this code we should avoid sending actual an email to user.
-   so we will create a mocking of send_welcome_email() function

###### Other benefit of Mocking
* Speed up tests

###### how to mock code
* Use *unitttest.mock* 
* magicMock/Mock - Replace real object
* patch - Overrides code for tests


