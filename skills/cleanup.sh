#!/bin/bash
# Skill para limpar traços de testes e manter ambiente limpo

set -e

PROJECT_ROOT="${1:-$HOME/test-automation-studio}"

echo "🧹 Limpando traços de testes em: $PROJECT_ROOT"

# Limpar screenshots do Selenium
find "$PROJECT_ROOT" -type f -name "*.png" -path "*/screenshots/*" -delete 2>/dev/null || true

# Limpar logs de testes
find "$PROJECT_ROOT" -type f -name "*.log" -delete 2>/dev/null || true

# Limpar reports HTML do Behave
find "$PROJECT_ROOT" -type d -name "reports" -exec rm -rf {} + 2>/dev/null || true

# Limpar cache do Python
find "$PROJECT_ROOT" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find "$PROJECT_ROOT" -type f -name "*.pyc" -delete 2>/dev/null || true

# Limpar arquivos temporários do Locust
find "$PROJECT_ROOT" -type f -name "*.dist" -delete 2>/dev/null || true

# Limpar diretórios .pytest_cache
find "$PROJECT_ROOT" -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

echo "✅ Ambiente limpo! Nenhum traço de teste restante."
