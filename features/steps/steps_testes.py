from re import U
from behave import *
from utils.validador import Validador
from utils.usuario import User

# email validate (emailEhValido)


@given('i have an e-mail {email}')
def step_impl(context, email):
    context.email = email


@when('i validate it')
def step_impl(context):
    context.result = Validador.emailEhValido(context.email)


@then('i should get {result}')
def step_impl(context, result):
    assert str(context.result) == result

# insert user (adiciona)


@given('i have an e-mail, password and name')
def step_impl(context):
    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"


@when('i insert it')
def step_impl(context):
    fakeDB = []
    user = User(fakeDB)
    context.result = user.adiciona(
        context.name, context.password, context.email)


@then('i should have the user inserted')
def step_impl(context):
    assert context.result is True


@given('i have an existent e-mail, password and name')
def step_impl(context):
    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"


@when('i try insert it again')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"}]
    user = User(fakeDB)

    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"

    context.result = user.adiciona(
        context.name, context.password, context.email)


@then('i should have a fail')
def step_impl(context):
    assert context.result is False


@given('i have an incorret e-mail, password and name')
def step_impl(context):
    context.name = "Novo usuario"
    context.email = "teste@teste.com"
    context.password = "123456"


@when('i try insert the invalid user')
def step_impl(context):
    fakeDB = []
    user = User(fakeDB)
    context.name = "Novo usuario"
    context.email = "teste@teste12315646"
    context.password = "123456"

    context.result = user.adiciona(
        context.name, context.password, context.email)


@then('i should have a fail insertion')
def step_impl(context):
    assert context.result is False

# search by id (busca_usuario_byid)


@given('i have an user id')
def step_impl(context):
    context.id = 1


@when('i search by id')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"}]
    user = User(fakeDB)

    context.result = user.busca_usuario_byid(context.id)


@then('i should have the user')
def step_impl(context):
    assert context.result == {"username": "Novo usuario",
                              "email": "teste@teste.com"}


@given('i have an user id inexistent')
def step_impl(context):
    context.id = 2


@when('i search by id inexistent')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"}]
    user = User(fakeDB)

    context.result = user.busca_usuario_byid(context.id)


@then('i should have fail')
def step_impl(context):
    assert context.result is False

# delete user (deleta_usuario_byid)


@given('i have an user id to delete')
def step_impl(context):
    context.id = 2


@when('i delete by id')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"},
              {"id": 2, "username": "Novo usuario 2",
               "email": "teste2@teste.com", "password": "654321"}]
    user = User(fakeDB)

    context.resultDelete = user.deleta_usuario_byid(context.id)
    context.searchId = user.busca_usuario_byid(context.id)


@ then('i should the user deleted')
def step_impl(context):
    assert context.resultDelete is True
    assert context.searchId is False


@given('i have an inexistent user id to delete')
def step_impl(context):
    context.id = 4


@when('i delete the inexistent user by id')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"},
              {"id": 2, "username": "Novo usuario 2",
               "email": "teste2@teste.com", "password": "654321"}]
    user = User(fakeDB)

    context.result = user.deleta_usuario_byid(context.id)


@then('i should the user deleted fail')
def step_impl(context):
    assert context.result is False

# listar usuários (exibir_todos)


@when('i list all user')
def step_impl(context):
    fakeDB = [{"id": 1, "username": "Novo usuario",
               "email": "teste@teste.com", "password": "123456"},
              {"id": 2, "username": "Novo usuario 2",
               "email": "teste2@teste.com", "password": "654321"},
              {"id": 3, "username": "Novo usuario 2",
               "email": "teste2@teste.com", "password": "654321"},
              {"id": 4, "username": "Novo usuario 2",
               "email": "teste2@teste.com", "password": "654321"},
              {"id": 5, "username": "Novo usuario 2",
               "email": "teste2@teste.com", "password": "654321"}]
    user = User(fakeDB)

    context.result = user.exibir_todos()


@then('i should have a list with all user')
def step_impl(context):
    assert context.result == [{"id": 1, "username": "Novo usuario",
                               "email": "teste@teste.com", "password": "123456"},
                              {"id": 2, "username": "Novo usuario 2",
                               "email": "teste2@teste.com", "password": "654321"},
                              {"id": 3, "username": "Novo usuario 2",
                               "email": "teste2@teste.com", "password": "654321"},
                              {"id": 4, "username": "Novo usuario 2",
                               "email": "teste2@teste.com", "password": "654321"},
                              {"id": 5, "username": "Novo usuario 2",
                               "email": "teste2@teste.com", "password": "654321"}]


@when('i try list all user in a empty list')
def step_impl(context):
    fakeDB = []
    user = User(fakeDB)

    context.result = user.exibir_todos()


@then('i should have empty list')
def step_impl(context):
    assert context.result == []
