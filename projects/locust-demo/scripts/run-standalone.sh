#!/bin/bash
# Executa Locust em modo standalone (sem master/worker)

set -e

mkdir -p results

echo "🚀 Iniciando Locust em modo STANDALONE..."
echo "📊 Web UI disponível em: http://localhost:8089"
echo ""
echo "🔧 Configuração:"
echo "  - Users: 50"
echo "  - Spawn rate: 5 users/s"
echo "  - Run time: 30s"
echo ""

locust -f locustfile.py \
    --host=https://the-internet.herokuapp.com \
    --users=50 \
    --spawn-rate=5 \
    --run-time=30s \
    --headless \
    --csv=results/standalone_results \
    --html=results/standalone_report.html \
    --logfile=results/standalone.log

echo ""
echo "✅ Teste finalizado!"
echo "📁 Resultados salvos em: results/"
echo ""
echo "📊 Estatísticas:"
cat results/standalone_results_stats.csv | head -20
