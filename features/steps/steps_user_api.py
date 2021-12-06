import requests
from behave import given, when, then
from json import dumps


@given('the URL_API is set to "{url_parameter}"')
def set_url(context, url_parameter):
    context.url = url_parameter


@given('i have the following users to enter')
def get_users(context):
    context.users = list()
    for item in context.table.rows:
        context.users.append(dict(item.items()))


@when('i send a post request with these users')
def insert_user(context):
    context.result = requests.post(
        f'{context.url}/user', data=dumps(context.users[0]))


@then('the users should be inserted')
def assert_inserted_user(context):
    print(context.result.text)
    assert "Usuário criado" in context.result.text


@given('i have an user_id')
def get_user_id(context):
    context.userId = "1"


@when('i send a get request with these user id')
def get_user_by_id(context):
    context.result = requests.get(
        f'{context.url}/user/' + context.userId)


@then('the user should be returned')
def assert_user_returned(context):
    assert "joao@teste.com" in context.result.text
    assert "Joao" in context.result.text


@given('i have an inexistent user_id')
def set_id(context):
    context.userId = "101"


@when('i send a get request with these inexistent user id')
def get_user(context):
    context.result = requests.get(
        f'{context.url}/user/' + context.userId)


@then('the user should be returned fail mensage')
def assert_get_user_fail(context):
    assert "Usuário não encontrado" in context.result.text


@when('i send a get request to list users')
def get_user(context):
    context.result = requests.get(
        f'{context.url}/user/')


@then('the users should be listed')
def assert_get_user(context):
    assert not ("Usuário não encontrado" in context.result.text)


@given('i have an user_id to delete')
def delete_users(context):
    context.userId = "1"


@when('i send a get request to delete')
def delete_user(context):
    context.result = requests.delete(
        f'{context.url}/user/' + context.userId)


@then('the users should be delete')
def assert_deleted_user(context):
    assert "Usuário deletado com sucesso" in context.result.text


@given('i have the user to update')
def post_update(context):
    context.users = list()
    for item in context.table.rows:
        context.users.append(dict(item.items()))


@when('i send a post request with these users to update')
def insert_update_user(context):
    requests.post(
        f'{context.url}/user', data=dumps(context.users[0]))
    context.result = requests.put(
        f'{context.url}/user/1', data=dumps(context.users[0]))


@then('the user should be updated')
def assert_updated_user(context):
    print(context.result.text)
    assert "Usuário atualizado" in context.result.text


@when('i send a post request to update an inexistent user')
def update_user(context):
    context.result = requests.put(
        f'{context.url}/user/105', data=dumps({
            "username": "Joao",
            "email": "Joao@email.cokm"
        }))


@then('the return should be fail update')
def assert_updated_user(context):
    print(context.result.text)
    assert "Usuário não encontrado" in context.result.text
