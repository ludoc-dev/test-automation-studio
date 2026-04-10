#!/bin/bash
# Executa Locust em modo Worker

set -e

MASTER_HOST=${1:-"localhost"}

echo "🔧 Iniciando Locust WORKER..."
echo "🔗 Conectando ao master: $MASTER_HOST"
echo ""

locust -f locust-distributed.py \
    --worker \
    --master-host=$MASTER_HOST

echo "❌ Worker desconectado"
