Feature: Animal Class

Scenario: Insert a new Animal
    Given i have nome and raça of Animal
    """
        {
            "nome": "Lucas",
            "raça": "Bulldog Frances"
        }
    """
    When i insert this Animal
    Then the Animal should be inserted


Scenario: Search Animal by ID
    Given i have Animals in Data Base
    """
    [
        {
            "id": 1,
            "nome": "Astrid",
            "raça": "Gato Persa"
        },
        {
            "id": 2,
            "nome": "Luna",
            "raça": "Labrador"
        }
    ]
    """
    When i search this Animal by ID "1"
    Then the Animal "Astrid" must be returned


Scenario: Delete Animal by ID
    Given i have an Animal in Data Base
    """
    {
        "id": 1,
        "nome": "Belchior",
        "raça": "Canário"
    }
    """
    When i delete this Animal by ID "1"
    Then the Animal should be Deleted


Scenario: Update an Animal
    Given i have the Animal in Data Base
    """
    {
        "id": 1,
        "nome": "Belchior",
        "raça": "Canário"
    }
    """
    When i update the name of this Animal to "Raul Seixas"
    Then the name of Animal should be updated
