#!/bin/bash
# Executa Locust em modo Master

set -e

echo "🚀 Iniciando Locust MASTER..."
echo "📊 Web UI disponível em: http://localhost:8089"
echo ""
echo "🔧 Configuração:"
echo "  - Users: 100"
echo "  - Spawn rate: 10 users/s"
echo "  - Expect workers: 4"
echo ""
echo "📋 Para conectar workers:"
echo "  locust -f locust-distributed.py --worker --master-host=<master-ip>"
echo ""

locust -f locust-distributed.py \
    --master \
    --expect-workers=4 \
    --host=https://the-internet.herokuapp.com \
    --users=100 \
    --spawn-rate=10 \
    --headless \
    --run-time=1m \
    --csv=results/test_results \
    --html=results/report.html \
    --logfile=results/locust.log

echo ""
echo "✅ Teste finalizado!"
echo "📁 Resultados salvos em: results/"
