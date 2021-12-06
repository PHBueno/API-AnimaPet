Feature: Users API Endpoint

Background: Requirements of API Tests
    Given the URL_API is set to "http://127.0.0.1:8000"

Scenario: Create an User (api)
    Given i have the following users to enter
        | username     | email                   | password  |
        | Joao         | joao@teste.com          | 143787    |
        | Maria        | maria@teste.com         | 78985     |
        | Carlos       | carlos@teste.com        | 78985     |
        | Pedro        | pedro@teste.com         | 78985     |
        | Eduardo      | eduardo@teste.com       | 78985     |
    When i send a post request with these users
    Then the users should be inserted

Scenario: Search an User by id (api)
    Given i have an user_id
    When i send a get request with these user id
    Then the user should be returned

Scenario: Search an User by inexistent id (api)
    Given i have an inexistent user_id
    When i send a get request with these inexistent user id
    Then the user should be returned fail mensage

Scenario: List Users
    When i send a get request to list users
    Then the users should be listed

Scenario: Delete Users
    Given i have an user_id to delete
    When i send a get request to delete
    Then the users should be delete

Scenario: Update an User (api)
    Given i have the user to update
        | username               | email                 | password  |
        | Carlos Atualizado      | carlos@teste.com      | 78985     |
    When i send a post request with these users to update
    Then the user should be updated


Scenario: Update an User (api)
    When i send a post request to update an inexistent user
    Then the return should be fail update