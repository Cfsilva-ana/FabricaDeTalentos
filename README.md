# Sistema de Sensores

Sistema de monitoramento e gerenciamento de sensores ambientais desenvolvido em Python.

## Funcionalidades

- **Coleta de dados**: Simula leituras de 5 tipos de sensores
- **Armazenamento**: Salva dados em arquivo JSON
- **Relatórios**: Visualização de leituras individuais e completas
- **Interface**: Menu interativo via terminal

## Sensores Disponíveis

| ID | Tipo | Faixa de Valores |
|----|------|------------------|
| 1 | Temperatura | 15°C - 35°C |
| 2 | Umidade | 30% - 90% |
| 3 | Pressão | 980 - 1030 hPa |
| 4 | Luminosidade | 0 - 1000 lux |
| 5 | CO2 | 300 - 1000 ppm |

## Estrutura do Projeto

```
FabricaDeTalentos/
├── main.py              # Arquivo principal com interface
├── sensor.py            # Classes Sensor e GerenciadorSensores
├── armazenamento.py     # Classe ArmazenamentoDados
├── relatorio.py         # Classe GeradorRelatorio
├── dados_sensores.json  # Arquivo de dados (gerado automaticamente)
└── README.md           # Este arquivo
```

## Como Usar

1. **Executar o sistema**:
   ```bash
   python main.py
   ```

2. **Menu principal**:
   - `1` - Gerar informações (coleta 3 leituras de cada sensor)
   - `2` - Visualizar relatórios
   - `3` - Sair

3. **Menu de relatórios**:
   - `1-5` - Relatório individual por sensor
   - `6` - Relatório completo
   - `7` - Voltar

## Requisitos

- Python 3.6+
- Bibliotecas padrão: `json`, `random`, `datetime`, `typing`

## Exemplo de Uso

```python
from sensor import GerenciadorSensores
from armazenamento import ArmazenamentoDados

# Criar instâncias
gerenciador = GerenciadorSensores()
armazenamento = ArmazenamentoDados()

# Coletar leitura
leitura = gerenciador.coletar_leitura(1)  # Sensor de temperatura
armazenamento.salvar_leitura(leitura)
```

## Formato dos Dados

```json
{
  "sensor_id": 1,
  "tipo": "Temperatura",
  "valor": 23.5,
  "timestamp": "2024-01-15 14:30:25"
}
```