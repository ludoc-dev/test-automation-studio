Feature: Login System
  Como um usuário do sistema
  Quero fazer login com minhas credenciais
  Para acessar as funcionalidades protegidas

  Background:
    Given que estou na página de login

  Scenario: Login bem-sucedido
    When preencho username "tomsmith" e senha "SuperSecretPassword!"
    Then vejo mensagem de sucesso "You logged into a secure area!"
    And consigo ver o botão de logout

  Scenario: Login com senha incorreta
    When preencho username "tomsmith" e senha "senha_errada"
    Then vejo mensagem de erro "Your password is invalid!"

  Scenario: Login com usuário inexistente
    When preencho username "usuario_inexistente" e senha "qualquer_senha"
    Then vejo mensagem de erro "Your username is invalid!"

  Scenario Outline: Login com diferentes credenciais
    When preencho username "<username>" e senha "<password>"
    Then vejo resultado "<result>"

    Examples:
      | username           | password              | result        |
      | tomsmith           | SuperSecretPassword!  | success       |
      | tomsmith           | wrong_password        | error         |
      | invalid_user       | any_password          | error         |
