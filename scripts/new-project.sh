#!/bin/bash
# Script para criar novo projeto de testes

set -e

PROJECT_NAME=$1
PROJECTS_DIR="$HOME/test-automation-studio/projects"

if [ -z "$PROJECT_NAME" ]; then
    echo "❌ Uso: new-project.sh <nome-do-projeto>"
    exit 1
fi

PROJECT_DIR="$PROJECTS_DIR/$PROJECT_NAME"

echo "📦 Criando projeto: $PROJECT_NAME"

# Criar estrutura
mkdir -p "$PROJECT_DIR"/{features,steps,pages,utils,reports,screenshots}

# Criar arquivo .env
cat > "$PROJECT_DIR/.env" <<EOF
# Configurações do Projeto
BASE_URL=https://example.com
BROWSER=headlesschrome
SCREENSHOT_ON_FAILURE=true
EOF

# Criar requirements.txt
cat > "$PROJECT_DIR/requirements.txt" <<EOF
# BDD Framework
behave==1.2.6
selenium==4.15.2

# Page Objects
webdriver-manager==4.0.1

# Load Testing
locust==2.18.3

# Utilities
python-dotenv==1.0.0
pytest==7.4.3
allure-behave==2.13.5
EOF

# Criar behave.ini
cat > "$PROJECT_DIR/behave.ini" <<EOF
[behave]
format = html.pretty
stdout_capture = false
stderr_capture = false
show_timings = true
junit = true
junit_directory = reports
EOF

# Criar feature de exemplo
cat > "$PROJECT_DIR/features/example.feature" <<EOF
Feature: Testes E2E
  Como um usuário
  Quero acessar o sistema
  Para realizar minhas tarefas

  Scenario: Login bem-sucedido
    Given que estou na página de login
    When preencho credenciais válidas
    Then sou redirecionado para o dashboard
    And vejo mensagem de boas-vindas
EOF

echo "✅ Projeto criado em: $PROJECT_DIR"
echo ""
echo "📋 Próximos passos:"
echo "cd $PROJECT_DIR"
echo "pip install -r requirements.txt"
echo "behave"
