Feature: Animals API Endpoint

Background: Requirements of API Tests
    Given the URL is set to "http://127.0.0.1:8000"

Scenario: Create an Animal (api)
    Given i have the following animals to enter
        | nome   | raca       |
        | Astrid | Gato Persa |
        | Luna   | Labrador   |
    When i send a post request with these animals
    Then the animals should be inserted