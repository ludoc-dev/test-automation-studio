# Lições Aprendidas - Test Automation

## 🎯 Erros Cometidos e Correções

### 1. **Hooks no steps file** ❌
**Erro:** Coloquei `before_scenario` e `after_scenario` no arquivo `steps/login_steps.py`
**Problema:** Behave não reconhece hooks nos steps, apenas no `environment.py`
**Correção:** Mover hooks para `environment.py`

### 2. **Chrome Manager incompatível** ❌
**Erro:** Usei `webdriver_manager.ChromeDriverManager()` no ARM64
**Problema:** Driver baixado não era compatível com arquitetura ARM64
**Correção:** Usar Selenium Manager nativo `webdriver.Chrome()` (baixa driver automaticamente)

### 3. **Missing driver attribute in after_scenario** ❌
**Erro:** `context.driver.quit()` mesmo quando driver não foi criado
**Problema:** Se `before_scenario` falha, `context.driver` não existe
**Correção:** Verificar `hasattr(context, 'driver')` antes de fazer quit

### 4. **Formato inválido no behave.ini** ❌
**Erro:** `format = html.pretty` (formato obsoleto)
**Problema:** Behave 1.2.6 não suporta esse formato
**Correção:** Usar `format = pretty`

## 📋 Checklist para Próximos Projetos

- [ ] Criar `environment.py` com hooks
- [ ] Usar Selenium Manager (sem webdriver-manager)
- [ ] Adicionar `hasattr()` check em `after_scenario`
- [ ] Configurar `behave.ini` com formatos válidos
- [ ] Testar com headless=false para debug inicial

## 🚀 Setup Correto

```python
# environment.py
def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.login_page = LoginPage(context.driver)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Screenshot
        pass
    if hasattr(context, 'driver'):
        context.driver.quit()
```

## 🎉 Resultado Final

```
1 feature passed, 0 failed, 0 skipped
6 scenarios passed, 0 failed, 0 skipped
19 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m16.376s
```

**Ambiente de testes funcionando perfeitamente!**
