from json import loads
from behave import given, when, then
from utils.animal import Animal

#################################
# Scenario: Insert a new Animal #
#################################
@given('i have nome and raça of Animal')
def set_animal(context):
    context.animal = loads(context.text)

@when('i insert this Animal')
def insert_animal(context):
    NewAnimal = Animal([])
    context.created = NewAnimal.adiciona_animal(
        context.animal['nome'], 
        context.animal['raça']
    )


@then('the Animal should be inserted')
def assert_animal_inserted(context):
    assert context.created is True

#################################
# Scenario: Search Animal by ID #
#################################
@given('i have Animals in Data Base')
def animal_in_db(context):
    animal = loads(context.text) # Transforma o texto (no Given) em JSON 
    context.NewAnimal = Animal(animal)

@when('i search this Animal by ID "{animal_id}"')
def search_animal(context, animal_id):
    id = int(animal_id)
    context.animal = context.NewAnimal.busca_animal_byid(id)

@then('the Animal "{animal_name}" must be returned')
def return_animal(context, animal_name):
    assert animal_name in context.animal['nome']


#################################
# Scenario: Delete Animal by ID #
#################################
@given('i have an Animal in Data Base')
def set_animal_in_db(context):
    animal = loads(context.text) # Transforma o texto (no Given) em JSON 
    context.NewAnimal = Animal([animal])

@when('i delete this Animal by ID "{animal_id}"')
def delete_animal(context, animal_id):
    id = int(animal_id)
    context.deleted = context.NewAnimal.deleta_animal_byid(id)

@then('the Animal should be Deleted')
def assert_deleted_animal(context):
    assert context.deleted is True

##############################
# Scenario: Update an Animal #
##############################
@given('i have the Animal in Data Base')
def add_animal_db(context):
    animal = loads(context.text) # Transforma o texto (no Given) em JSON
    context.id = animal['id']
    context.raca = animal['raça']
    context.NewAnimal = Animal([animal])

@when('i update the name of this Animal to "{new_animal_name}"')
def update_animal(context, new_animal_name):
    context.updated = context.NewAnimal.atualiza_animal(context.id, new_animal_name, context.raca)

@then('the name of Animal should be updated')
def assert_animal_updated(context):
    assert context.updated is True