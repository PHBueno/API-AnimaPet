from re import U
from behave import given, when, then
from utils.validador import Validador
from utils.usuario import User

# email validate (emailEhValido)


@given('i have an e-mail {email}')
def get_email(context, email):
    context.email = email


@when('i validate it')
def valid_email(context):
    context.result = Validador.emailEhValido(context.email)


@then('i should get {result}')
def assert_email(context, result):
    assert str(context.result) == result

# insert user (adiciona)


@given('i have an e-mail, password and name')
def define_user_infos(context):
    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"


@when('i insert it')
def insert_user_infos(context):
    fakeDB = []
    user = User(fakeDB)
    context.result = user.adiciona(
        context.name, context.password, context.email)


@then('i should have the user inserted')
def assert_user_infos(context):
    assert context.result is True


@given('i have an existent e-mail, password and name')
def define_existent_infos(context):
    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"


@when('i try insert it again')
def insert_existent_infos(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"}]
    user = User(fakeDB)

    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"

    context.result = user.adiciona(
        context.name, context.password, context.email)


@then('i should have a fail')
def assert_existent_infos(context):
    assert context.result is False


@given('i have an incorret e-mail, password and name')
def define_incorret_infos(context):
    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"


@when('i try insert the invalid user')
def insert_incoret_infos(context):
    fakeDB = []
    user = User(fakeDB)
    context.name = "Novo usuario"
    context.email = "teste@teste12315646"
    context.password = "123456"

    context.result = user.adiciona(
        context.name, context.password, context.email)


@then('i should have a fail insertion')
def assert_incoret_infos(context):
    assert context.result is False

# search by id (busca_usuario_byid)


@given('i have an user id')
def define_user_id(context):
    context.id = 1


@when('i search by id')
def get_userid(context):
    fakeDB = [
        {
            "id": 1,
            "username": "Novo usuario",
            "email": "teste@teste.com",
            "password": "123456"
        }]
    user = User(fakeDB)

    context.result = user.busca_usuario_byid(context.id)


@then('i should have the user')
def assert_userid(context):
    assert context.result == {
        "username": "Novo usuario",
        "email": "teste@teste.com"
    }


@given('i have an user id inexistent')
def define_inexistent_id(context):
    context.id = 2


@when('i search by id inexistent')
def get_inexistent_id(context):
    fakeDB = [
        {
            "id": 1,
            "username": "Novo usuario",
            "email": "teste@teste.com",
            "password": "123456"
        }]
    user = User(fakeDB)

    context.result = user.busca_usuario_byid(context.id)


@then('i should have fail')
def assert_inexistent_id(context):
    assert context.result is False

# delete user (deleta_usuario_byid)


@given('i have an user id to delete')
def define_id_to_delete(context):
    context.id = 2


@when('i delete by id')
def delete_user_id(context):
    fakeDB = [
        {
            "id": 1,
            "username": "Novo usuario",
            "email": "teste@teste.com",
            "password": "123456"
        },
        {
            "id": 2,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        }]
    user = User(fakeDB)

    context.resultDelete = user.deleta_usuario_byid(context.id)
    context.searchId = user.busca_usuario_byid(context.id)


@then('i should the user deleted')
def assert_delete_user_id(context):
    assert context.resultDelete is True
    assert context.searchId is False


@given('i have an inexistent user id to delete')
def define_inexistent_id_delete(context):
    context.id = 4


@when('i delete the inexistent user by id')
def delete_inexistent_user(context):
    fakeDB = [
        {
            "id": 1,
            "username": "Novo usuario",
            "email": "teste@teste.com",
            "password": "123456"
        },
        {
            "id": 2,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        }]
    user = User(fakeDB)

    context.result = user.deleta_usuario_byid(context.id)


@then('i should the user deleted fail')
def assert_delete_inexistent_id(context):
    assert context.result is False

# listar usuários (exibir_todos)


@when('i list all user')
def list_users(context):
    fakeDB = [
        {
            "id": 1,
            "username": "Novo usuario",
            "email": "teste@teste.com",
            "password": "123456"
        },
        {
            "id": 2,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        },
        {
            "id": 3,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        },
        {
            "id": 4,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        },
        {
            "id": 5,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        }]
    user = User(fakeDB)

    context.result = user.exibir_todos()


@then('i should have a list with all user')
def assert_all_users(context):
    assert context.result == [
        {
            "id": 1,
            "username": "Novo usuario",
            "email": "teste@teste.com",
            "password": "123456"
        },
        {
            "id": 2,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        },
        {
            "id": 3,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        },
        {
            "id": 4,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        },
        {
            "id": 5,
            "username": "Novo usuario 2",
            "email": "teste2@teste.com",
            "password": "654321"
        }]


@when('i try list all user in a empty list')
def no_users_exists(context):
    fakeDB = []
    user = User(fakeDB)

    context.result = user.exibir_todos()


@then('i should have empty list')
def assert_users_empty(context):
    assert context.result == []

# User update (atualiza_usuario)


@given('i have a id and new name or email')
def step_impl(context):
    context.id = 1
    context.newName = "nome usuario atualizado"
    context.newEmail = "teste@testeatualizado.com"


@when('i update user')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"}]
    user = User(fakeDB)

    context.updateResult = user.atualiza_usuario(
        context.id, context.newName, context.newEmail)
    context.searchResult = user.busca_usuario_byid(context.id)


@then('i should have the user updated')
def step_impl(context):
    assert context.updateResult is True
    assert context.searchResult == {"username": context.newName,
                                    "email": context.newEmail}


@when('i try update inexistent user')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"}]
    user = User(fakeDB)

    context.result = user.atualiza_usuario(
        5, context.newName, context.newEmail)


@then('i should have the user updated fail')
def step_impl(context):
    assert context.result is False
