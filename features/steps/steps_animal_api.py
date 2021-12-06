import requests
from json import dump, dumps, loads
from behave import given, when, then

####################################
# Scenario: Create an Animal (api) #
####################################
@given('the URL is set to "{url_parameter}"')
def set_url(context, url_parameter):
    context.url = url_parameter


@given('i have the following animals to enter')
def get_animals(context):
    context.animals = list()
    for item in context.table.rows:
        context.animals.append(dict(item.items()))

@when('i send a POST request to /animais with these animals')
def insert_animal(context):
    for animal in context.animals:
        context.result = requests.post(
            f'{context.url}/animais', 
            data=dumps(animal)
        )

@then('the animals should be inserted')
def assert_inserted_animal(context):
    assert context.result.status_code == 200

#######################################
# Scenario: Search Animal by ID (api) #
#######################################
@given('the Animal with id "{animal_id}" is in Data Base')
def define_animal_id(context, animal_id):
    context.animal_id = animal_id

@when('i send a GET request to /animais/id_animal')
def get_animal(context):
    context.result = requests.get(
        f'{context.url}/animais/{context.animal_id}'
    )

@then('the Animal should be returned')
def assert_returned_animal(context):
    assert context.result.status_code == 200

################################
# Scenario: Return all animals #
################################
@given('i have animals on DB')
def insert_animals_on_DB(context):
    context.animals = list()
    for item in context.table.rows:
        context.animals.append(dict(item.items()))

    for animal in context.animals:
        context.result = requests.post(
            f'{context.url}/animais', 
            data=dumps(animal)
        )

@when('i send a GET request to /animais')
def get_all_animals(context):
    context.result = requests.get(
        f'{context.url}/animais'
    )

@then('all Animals should be returned')
def assert_get_all_animals(context):
    assert len(loads(context.result.text)) > 1

##############################
# Scenario: Delete an Animal #
##############################
@given('i wanted to delete the animal with id "{id_animal}"')
def get_id_to_delete(context, id_animal):
    context.id = id_animal

@when('i send a DELETE request to /animais/id_animal')
def delete_animal(context):
    context.result = requests.delete(
        f'{context.url}/animais/{context.id}'
    )

@then('the Animal with id should be deleted')
def assert_deleted_animal(context):
    assert context.result.status_code == 200

####################################
# Scenario: Update an Animal (api) #
####################################
@given('i wanted to search the animal with id "{id_animal}"')
def get_animal_id(context, id_animal):
    context.id = id_animal

@when('i send a PUT request to /animais with this json')
def update_animal(context):
    context.new_animal = loads(context.text)

    context.result = requests.put(
        f'{context.url}/animais?id_animal={context.id}',
        data=dumps(context.new_animal)
    )

@then('the Animal with id should be updated')
def assert_animal_updated(context):
    print(dumps(context.new_animal))
    assert context.result.status_code == 200
    
