Feature: Animals API Endpoint

Background: Requirements of API Tests
    Given the URL is set to "http://127.0.0.1:8000"

Scenario: Create an Animal (api)
    Given i have the following animals to enter

        | nome   | raca       |
        | Astrid | Gato Persa |
        | Luna   | Labrador   |

    When i send a POST request to /animais with these animals
    Then the animals should be inserted

Scenario: Search Animal by ID (api)
    Given the Animal with id "1" is in Data Base
    When i send a GET request to /animais/id_animal
    Then the Animal should be returned


Scenario: Return all animals (api)
    Given i have animals on DB

        | nome   | raca          |
        | Bella  | Gato Persa    |
        | Tita   | Pastor alemão |

    When i send a GET request to /animais
    Then all Animals should be returned

Scenario: Delete an Animal (api)
    Given i wanted to delete the animal with id "2"
    When i send a DELETE request to /animais/id_animal
    Then the Animal with id should be deleted

Scenario: Update an Animal (api)
    Given i wanted to search the animal with id "3"
    When i send a PUT request to /animais with this json
        """
        {
            "nome": "Belchior",
            "raca": "Gato Persa"
        }
        """
    Then the Animal with id should be updated