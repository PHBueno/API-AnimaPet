Feature: tests

  Scenario Outline: run a simple test
    Given i have an e-mail <email>
    When i validate it
    Then i should get <status>

Examples: valid e-mails
    | email                    | status |
    | teste@teste.com          | True   |
    | teste123@teste.com       | True   |
    | teste123@teste.com.br    | True   |
    | teste123@teste123.com.br | True   |
    | teste123@abcde.com.br    | True   |

Examples: invalid e-mails
    | email                               | status  |
    | teste@@$#@%$.com                    | False   |
    | teste123@teste.s                    | False   |
    | #%$#%3@teste.com.br                 | False   |
    | teste123@abcde                      | False   |
    | teste123@abcde.$                    | False   | 


Scenario: run a simple to insert an user
    Given i have an e-mail, password and name
    When i insert it
    Then i should have the user inserted

Scenario: run a simple to insert an user (fail)
    Given i have an existent e-mail, password and name 
    When i try insert it again
    Then i should have a fail

Scenario: run a simple to insert an user (fail)
    Given i have an incorret e-mail, password and name 
    When i try insert the invalid user
    Then i should have a fail insertion

Scenario: run a simple to search an user by id
    Given i have an user id 
    When i search by id
    Then i should have the user

Scenario: run a simple to search an inexistent user by id
    Given i have an user id inexistent 
    When i search by id inexistent
    Then i should have fail

Scenario: run a simple to delete an user
    Given i have an user id to delete
    When i delete by id
    Then i should the user deleted

Scenario: run a simple to delete an inexistent user
    Given i have an inexistent user id to delete
    When i delete the inexistent user by id 
    Then i should the user deleted fail

Scenario: run a simple to list all users
    When i list all user 
    Then i should have a list with all user

Scenario: run a simple to list all user whan is empty
    When i try list all user in a empty list
    Then i should have empty list