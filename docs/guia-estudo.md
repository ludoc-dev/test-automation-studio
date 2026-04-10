# Guia de Estudo: Test Automation

📚 **Documentação Extraída via `web2md`**

## 📖 Recursos Disponíveis

### 1. Behave (BDD Framework)

- **Arquivo:** `behave-docs.md`
- **Conteúdo:** Tutorial completo, features, step implementations, environmental controls
- **Tópicos:**
  - Feature files e Gherkin syntax
  - Python step implementations
  - Environmental controls
  - Tags e fixtures
  - Debug-on-error

### 2. Selenium WebDriver

- **Arquivo:** `selenium-docs.md`
- **Conteúdo:** WebDriver basics, elements, actions API
- **Tópicos:**
  - Getting started
  - Web elements (DOM)
  - Actions API
  - Support features
  - Troubleshooting

### 3. Locust (Load Testing)

- **Arquivo:** `locust-docs.md`
- **Conteúdo:** Documentação principal do Locust
- **Tópicos:**
  - HttpUser e tasks
  - Distribuição de carga
  - Métricas e monitoring

## 🎯 Roadmap de Estudo

### Semana 1: Behave + Gherkin

1. Ler `behave-docs.md` - seção Tutorial
2. Criar primeiro projeto com `./scripts/new-project.sh teste1`
3. Implementar feature file simples
4. Escrever steps em Python

### Semana 2: Selenium WebDriver

1. Ler `selenium-docs.md`
2. Instalar Selenium: `pip install selenium webdriver-manager`
3. Criar Page Objects básicos
4. Implementar waits explícitos

### Semana 3: Integração Behave + Selenium

1. Combinar features com Page Objects
2. Implementar hooks (before/after scenario)
3. Adicionar screenshots em falhas
4. Organizar estrutura de diretórios

### Semana 4: Locust

1. Ler `locust-docs.md`
2. Instalar Locust: `pip install locust`
3. Criar primeiro teste de carga
4. Executar em modo distribuído

### Semana 5: GitLab CI/CD

1. Criar `.gitlab-ci.yml`
2. Configurar pipeline stages
3. Integrar testes automatizados
4. Configurar quality gates

## 🚀 Comandos Úteis

```bash
# Criar novo projeto
cd ~/test-automation-studio
./scripts/new-project.sh meu-projeto

# Limpar ambiente
./skills/cleanup.sh

# Extrair mais documentação
cd ~/web2md
bun run web2md.ts <URL> --out novo-doc.md

# Executar testes Behave
cd ~/test-automation-studio/projects/<projeto>
behave

# Executar Locust
locust -f locustfile.py --host https://example.com
```

## 📋 Próximos Passos

1. **Estudar documentação extraída**
2. **Criar projeto prático**
3. **Implementar testes reais**
4. **Configurar CI/CD**

---

**Dica:** Use `web2md` para extrair mais documentação conforme necessário!
