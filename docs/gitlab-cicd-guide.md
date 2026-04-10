# GitLab CI/CD para Test Automation

## 🚀 Pipeline Completo

O pipeline `.gitlab-ci.yml` implementa 4 stages principais:

### 1. **Test Stage** - Testes Funcionais

```yaml
unit-tests:
  stage: test
  script:
    - behave --format=pretty --junit
  artifacts:
    reports:
      junit: projects/demo-login/reports/*.xml
```

**Features:**
- Executa testes Behave em paralelo
- Gera relatórios JUnit para o GitLab
- Salva screenshots em falhas
- Cache de dependências Python

### 2. **Load-Test Stage** - Testes de Carga

```yaml
load-test-smoke:
  stage: load-test
  script:
    - locust -f locustfile.py --headless --users=10
  artifacts:
    reports:
      html: projects/locust-demo/results/report.html
```

**Features:**
- Teste de fumaça automático (10 users)
- Teste de estresse manual (100 users)
- Relatórios HTML do Locust
- Thresholds de performance

### 3. **Report Stage** - Quality Gates

```yaml
quality-gate:
  stage: report
  script:
    - pytest --cov=pages --cov-report=xml
  coverage: '/TOTAL.*\s+(\d+%)$/'
```

**Features:**
- Cobertura de código mínimo 80%
- Relatórios de cobertura HTML/XML
- Badge de cobertura no README

### 4. **Deploy Stage** - Deploy Automatizado

```yaml
deploy-staging:
  stage: deploy
  environment:
    name: staging
  script:
    - scp -r pages/ user@server:/app/
```

**Features:**
- Deploy automático para staging
- Deploy manual para produção
- Integração com ambientes GitLab

## 🔧 Configuração de Ambientes

### Adicionar variáveis no GitLab:

**Settings → CI/CD → Variables:**
```
STAGING_SERVER=staging.example.com
PRODUCTION_SERVER=production.example.com
SSH_PRIVATE_KEY=<chave-ssh>
```

### Configurar Runners:

```bash
# Registrar runner com Docker
gitlab-runner register \
  --url https://gitlab.com/ \
  --registration-token <token> \
  --executor docker \
  --docker-image python:3.11
```

## 📊 Relatórios e Métricas

### JUnit Reports

O GitLab lê relatórios JUnit e mostra:
- ✅ Pass rate por teste
- ⏱️ Duração dos testes
- ❌ Falhas com stack trace

### Coverage Reports

```yaml
artifacts:
  reports:
    coverage_report:
      coverage_format: cobertura
      path: coverage.xml
```

Mostra badge no README:
```markdown
![coverage](https://gitlab.com/user/badges/main/coverage.svg)
```

### HTML Reports

```yaml
artifacts:
  reports:
    html: results/report.html
```

Botão "Browse" no job artifacts.

## 🎯 Paralelização

### Por Features:

```yaml
test-parallel:
  parallel: 4
  script:
    - behave --processes=4
```

### Por Stages:

```yaml
test-a:
  script: behave --tags=@smoke
test-b:
  script: behave --tags=@regression
```

## 🚨 Quality Gates

### Regras de Falha:

```yaml
test-job:
  allow_failure: false  # Falha o pipeline

load-test:
  allow_failure: true   # Avisa mas não falha
```

### Thresholds de Performance:

```python
# locustfile.py
@events.request.add_listener
def on_request(..., **kwargs):
    if response_time > 1000:
        print(f"⚠️ Slow request: {response_time}ms")
```

## 📅 Schedules

**CI/CD → Schedules:**
```yaml
nightly-tests:
  only:
    variables:
      - $CI_PIPELINE_SOURCE == "schedule"
  script:
    - behave --tags=@nightly
```

Criar schedule:
1. CI/CD → Schedules → New schedule
2. Pattern: `0 2 * * *` (2 da manhã)
3. Trigger: `nightly-tests`

## 🔐 Segurança

### Secrets Management:

```yaml
before_script:
  - export LOGIN_USER=$TEST_USER
  - export LOGIN_PASS=$TEST_PASS
```

### Masked Variables:

**Settings → CI/CD → Variables:**
- ✅ Masked: Esconde valor nos logs
- ✅ Protected: Apenas branches protegidos
- ✅ Expanded: Disponível como env var

## 🎯 Exemplos de Uso

### Trigger Manual:

```yaml
stress-test:
  when: manual
  script:
    - locust --users=1000
```

### Conditional Execution:

```yaml
deploy-prod:
  only:
    - main
  when: manual
  only:
    variables:
      - $DEPLOY_ENABLED == "true"
```

### Multi-Project:

```yaml
test-api:
  trigger:
    project: api-tests
    branch: main
    strategy: depend
```

## 📱 Notificações

### Slack Integration:

**Settings → Integrations → Slack:**
```yaml
notifications:
  slack:
    channels:
      - "#testing"
    on_success: true
    on_failure: true
```

### Email:

```yaml
notify:
  script:
    - mail -s "Pipeline $CI_PIPELINE_ID" team@example.com
```

## 🎓 Boas Práticas

1. **Artifacts:** Expiração de 7-30 dias
2. **Cache:** Dependências entre pipelines
3. **Parallel:** Múltiplos testes simultâneos
4. **Manual:** Deploy e testes pesados
5. **Protected:** Produção e secrets
6. **Coverage:** Quality gate mínimo 80%
7. **Schedules:** Testes noturnos/periódicos
