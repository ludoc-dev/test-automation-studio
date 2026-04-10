from behave import given, when, then
from pages.login_page import LoginPage


@given('que estou na página de login')
def step_impl(context):
    context.login_page.open()


@when('preencho username "{username}" e senha "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@then('vejo mensagem de sucesso "{message}"')
def step_impl(context, message):
    assert context.login_page.is_login_successful(), "Login não foi bem-sucedido"
    flash_message = context.login_page.get_flash_message()
    assert message in flash_message, f"Mensagem esperada: {message}, Mensagem recebida: {flash_message}"


@then('vejo mensagem de erro "{message}"')
def step_impl(context, message):
    assert context.login_page.is_login_failed(), "Erro não foi mostrado"
    flash_message = context.login_page.get_flash_message()
    assert message in flash_message, f"Mensagem esperada: {message}, Mensagem recebida: {flash_message}"


@then('consigo ver o botão de logout')
def step_impl(context):
    assert context.login_page.is_visible(context.login_page.logout_button), "Botão de logout não está visível"


@then('vejo resultado "{result}"')
def step_impl(context, result):
    if result == "success":
        assert context.login_page.is_login_successful(), "Login deveria ter sido bem-sucedido"
    else:
        assert context.login_page.is_login_failed(), "Login deveria ter falhado"
