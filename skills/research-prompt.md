# Prompt de Pesquisa: Test Automation Roadmap

## Contexto
Você é um agente de pesquisa especializado em engenharia de testes automatizados. Precisa mapear o caminho completo de aprendizado desde BDD até testes de carga e CI/CD.

## Objetivo
Criar um roadmap estruturado e pragmático para desenvolvimento autônomo em testes automatizados, focando em:

1. **BDD com Behave e Selenium**
   - Gherkin syntax avançada
   - Page Object Model (POM)
   - Design patterns para testes
   - Boas práticas de organização

2. **Testes de Carga com Locust**
   - Arquitetura distribuída
   - Cenários realistas
   - Métricas e análise
   - Integração com monitoring

3. **CI/CD com GitLab**
   - Pipeline configuration
   - Test automation em CI
   - Deploy automatizado
   - Quality gates

## Deliverables Esperados

### 1. Roadmap Estruturado
- Sequência lógica de aprendizado
- Dependências entre tópicos
- Estimativa de tempo por fase
- Recursos recomendados (docs, tutoriais, vídeos)

### 2. Código de Exemplo
- Feature files Gherkin completos
- Implementação de Page Objects
- Testes Selenium funcionais
- Scripts Locust para carga
- Pipeline GitLab CI/CD

### 3. Boas Práticas
- Organização de diretórios
- Padrões de nomenclatura
- Tratamento de erros
- Estratégias de manutenção

### 4. Arquitetura de Referência
- Estrutura de projeto escalável
- Separação de responsabilidades
- Configuração de ambientes
- Estratégias de paralelização

## Requisitos Específicos

### Behave + Selenium
- Como estruturar feature files complexos
- Implementação de POM robusto
- Gerenciamento de estados entre steps
- Tratamento de elementos dinâmicos
- Strategies para waits explícitos/implícitos

### Locust
- Como modelar comportamento de usuário real
- Distribuição de carga em múltiplas máquinas
- Extração e análise de métricas
- Integração com APM tools

### GitLab CI/CD
- Pipeline stages para testes
- Parallel execution
- Report generation
- Failure handling
- Deployment automation

## Formato de Resposta

1. **Roadmap Visual** (ASCII art ou mermaid)
2. **Código Comentado** (Python + YAML)
3. **Checklist Prático** (o que implementar primeiro)
4. **Resources por Fase** (links oficiais + comunidade)
5. **Common Pitfalls** (erros comuns e como evitar)

## Restrições

- Foco em Python + Selenium + Behave + Locust + GitLab
- Não incluir ferramentas alternativas (ex: não mencionar Cypress, Playwright, k6)
- Código deve ser production-ready, não apenas "hello world"
- Incluir tratamento de erros realista
- Considerar performance e manutenibilidade

---

**Execute pesquisa web profunda e retorne um guia completo implementável.**
