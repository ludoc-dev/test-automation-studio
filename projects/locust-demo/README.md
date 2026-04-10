# Locust Load Testing Demo

Testes de carga com Locust - modo standalone e distribuído.

## 🚀 Modos de Execução

### 1. Standalone (Single Machine)

```bash
cd ~/test-automation-studio/projects/locust-demo
./scripts/run-standalone.sh
```

**Configuração:**
- 50 usuários simultâneos
- 5 usuários/segundo
- Duração: 30 segundos

### 2. Distribuído (Master + Workers)

#### Master:
```bash
./scripts/run-master.sh
```

#### Workers (em múltiplas máquinas):
```bash
./scripts/run-worker.sh <master-ip>
# ou
./scripts/run-worker.sh 192.168.1.100
```

**Configuração:**
- 100 usuários simultâneos
- 10 usuários/segundo
- 4 workers esperados
- Duração: 1 minuto

## 📊 Resultados

Os resultados são salvos em `results/`:
- `test_results_stats.csv` - Estatísticas detalhadas
- `test_results_stats_history.csv` - Histórico temporal
- `test_results_failures.csv` - Falhas ocorridas
- `report.html` - Relatório visual
- `locust.log` - Logs completos

## 🎯 Scenarios

### WebsiteUser
- **login_logout** (weight: 3): Fluxo completo de autenticação
- **view_pages** (weight: 2): Navegação por páginas
- **status_codes** (weight: 1): Verificação de status codes

### APIUser
- **get_posts**: Busca posts (GET)
- **get_users**: Busca usuários (GET)
- **create_post** (weight: 2): Cria post (POST)

## 📈 Métricas Importantes

- **RPS (Requests Per Second):** Taxa de requisições
- **Response Time:** Tempo de resposta médio
- **Failure Rate:** Taxa de falhas
- **RPS/Fail Ratio:** Relação sucesso/falha

## 🔧 Configuração

Edite `config/locust.conf` para ajustar parâmetros:
```ini
[locust]
users = 100
spawn-rate = 10
run-time = 1m
expect-workers = 4
```
