###### Testing in django

-   Django has a testing suite built into it

*   it is built on top unit testing framework called _unittest_
*   Django Testing suit has some additional features that make it easier to test

    -   Test client - dummy web browser
    -   simulated authentication
    -   Temporary Databases

*   Django Rest framework add some feature also
    -   API test client

###### Where to write tests code

-   generally tests.py is the file we use to write test
-   or we can use tests/ directory to run test.
    **But we can not use both** at the same time

*   Test modules must start with test\_
*   Test directory must contains \_\_init\_\_.py

###### Test Database
* Test code that uses the DB
* Specific database for tests

###### Test Classes 
* SimpleTestCase
    * No database integration
    * Useful if no database is required for your test
    * Save time executing tests
* TestCase
    * Database integration
    * useful for testing code that uses the database


###### Writing tests
* Import test class
    * SimpleTestCase - No Database
    * TestCase - database
* Import objects to test
* Define test class
* Add test method( prefix the method test_)
* Executed code to be tested
* Check output
