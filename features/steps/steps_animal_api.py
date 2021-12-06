import requests
from behave import given, when, then
from json import dumps

@given('the URL is set to "{url_parameter}"')
def set_url(context, url_parameter):
    context.url = url_parameter

@given('i have the following animals to enter')
def get_animals(context):
    context.animals = list()
    for item in context.table.rows:
        context.animals.append(dict(item.items()))

@when('i send a post request with these animals')
def insert_animal(context):
    context.result = requests.post(f'{context.url}/animais', data=dumps(context.animals[0]))

@then('the animals should be inserted')
def assert_inserted_animal(context):
    print(context.result.text)
    assert "Animal inserido" in context.result.text