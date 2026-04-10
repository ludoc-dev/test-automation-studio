# Padrões Avançados de Teste

## 🎯 Behave - Padrões Avançados

### 1. Scenario Outlines com Examples

```gherkin
Feature: Busca de Produtos

  Scenario Outline: Buscar produtos por categoria
    Given que estou na página de busca
    When preencho categoria "<categoria>"
    Then vejo "<resultado>" resultados

    Examples:
      | categoria  | resultado |
      | eletrônicos| 150       |
      | livros     | 89        |
      | roupas     | 234       |
```

**Vantagem:** Um cenário, múltiplos testes

### 2. Backgrounds para Setup Comum

```gherkin
Feature: Gestão de Usuários

  Background:
    Given que estou autenticado como admin
    E estou na página de gestão

  Scenario: Criar novo usuário
    When clico em "Novo Usuário"
    Then vejo formulário de criação

  Scenario: Editar usuário
    When clico em "Editar"
    Then vejo formulário de edição
```

**Vantagem:** Elimina duplicação de steps

### 3. Tags e Filtragem

```gherkin
@smoke @critical
Scenario: Login básico
  When faço login
  Then acesso o sistema

@regression @slow
Scenario: Processamento batch
  When executo processamento
  Then vejo resultado final
```

**Execução:**
```bash
behave --tags=smoke
behave --tags="not slow"
behave --tags="smoke and not critical"
```

### 4. Tables para Dados Complexos

```gherkin
Scenario: Cadastro de múltiplos produtos
  When cadastro os produtos:
    | nome     | preco  | estoque |
    | Produto A| 99.90  | 100     |
    | Produto B| 149.90 | 50      |
    | Produto C| 49.90  | 200     |
  Then vejo mensagem "3 produtos criados"
```

### 5. Hooks Avançados

```python
# environment.py

def before_all(context):
    """Executa uma vez antes de todos os cenários"""
    context.config = load_config()

def before_feature(context, feature):
    """Executa antes de cada feature"""
    context.logger = setup_logger(feature.name)

def before_scenario(context, scenario):
    """Executa antes de cada cenário"""
    if "slow" in scenario.tags:
        context.timeout = 60

def after_step(context, step):
    """Executa após cada step"""
    if step.status == "failed":
        context.driver.save_screenshot(f"{step.name}.png")
```

## 🏗️ Selenium - Design Patterns

### 1. Page Object Factory

```python
class PageFactory:
    @staticmethod
    def get_page(driver, page_name):
        pages = {
            "login": LoginPage,
            "dashboard": DashboardPage,
            "settings": SettingsPage
        }
        return pages[page_name](driver)

# Uso
login_page = PageFactory.get_page(driver, "login")
```

### 2. Fluent Interface

```python
class LoginPage(BasePage):
    def login(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.login_button)
        return DashboardPage(self.driver)

# Uso
dashboard = LoginPage(driver).open().login("user", "pass")
```

### 3. Component Object Pattern

```python
class DataTable:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def get_row_count(self):
        return len(self.driver.find_elements(*self.locator))

    def get_cell_text(self, row, col):
        # Lógica para acessar célula específica
        pass

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.products_table = DataTable(driver, (By.ID, "products"))
```

### 4. Strategy Pattern para Waits

```python
class WaitStrategy:
    def wait(self, driver, locator):
        pass

class ExplicitWait(WaitStrategy):
    def wait(self, driver, locator):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )

class FluentWait(WaitStrategy):
    def wait(self, driver, locator):
        return WebDriverWait(driver, 30, poll_frequency=1).until(
            EC.presence_of_element_located(locator)
        )

class Element:
    def __init__(self, locator, wait_strategy):
        self.locator = locator
        self.wait_strategy = wait_strategy

    def find(self, driver):
        return self.wait_strategy.wait(driver, self.locator)
```

### 5. Configuration Management

```python
# config/environments.yml
production:
  base_url: "https://prod.example.com"
  timeout: 30
  headless: true

staging:
  base_url: "https://staging.example.com"
  timeout: 20
  headless: false

# config/config.py
class Config:
    def __init__(self, env="staging"):
        with open(f"config/environments.yml") as f:
            self.config = yaml.safe_load(f)[env]

    @property
    def base_url(self):
        return self.config["base_url"]
```

## 🎭 Padrões Comportamentais

### 1. Chain of Responsibility para Steps

```python
class StepHandler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, context):
        if self.next_handler:
            return self.next_handler.handle(context)
        return True

class AuthenticationHandler(StepHandler):
    def handle(self, context):
        if not context.logged_in:
            context.login_page.login()
        return super().handle(context)
```

### 2. Observer Pattern para Eventos

```python
class TestEventObserver:
    def on_test_start(self, test_name):
        pass

    def on_test_complete(self, test_name, result):
        pass

    def on_test_failure(self, test_name, error):
        pass

class MetricsObserver(TestEventObserver):
    def on_test_complete(self, test_name, result):
        self.metrics.record(test_name, result.duration)
```

## 📦 Estrutura de Projeto Enterprise

```
project/
├── config/
│   ├── environments.yml
│   └── locust.conf
├── pages/
│   ├── base_page.py
│   ├── components/
│   │   ├── table.py
│   │   └── form.py
│   └── pages/
│       ├── login_page.py
│       └── dashboard_page.py
├── steps/
│   ├── login_steps.py
│   └── common_steps.py
├── utils/
│   ├── driver_factory.py
│   ├── config_loader.py
│   └── screenshot_helper.py
├── features/
│   └── *.feature
└── environment.py
```

## 🔧 Best Practices

1. **DRY (Don't Repeat Yourself):** Reuse steps and page objects
2. **Single Responsibility:** Each class/method does one thing
3. **Explicit Waits:** Never use `time.sleep()`
4. **Semantic Locators:** Use data attributes instead of CSS/XPath
5. **Fail Fast:** Assert early and clearly
6. **Isolation:** Tests should not depend on each other
7. **Clean State:** Reset database/state between tests
