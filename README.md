# Sistema de Sensores

Sistema de monitoramento e gerenciamento de sensores ambientais desenvolvido em Python com arquitetura orientada a objetos.

## Funcionalidades

- **Coleta de dados**: Simula leituras de 5 tipos de sensores usando herança e polimorfismo
- **Armazenamento**: Salva dados em arquivo JSON com tratamento robusto de exceções
- **Relatórios**: Visualização de leituras individuais, completas e estatísticas
- **Interface**: Menu interativo via terminal com validações
- **Tratamento de Exceções**: Validações completas e mensagens de erro informativas

## Arquitetura do Sistema

### Herança e Polimorfismo
- **SensorBase**: Classe abstrata base para todos os sensores
- **Classes Específicas**: SensorTemperatura, SensorUmidade, SensorPressao, SensorLuminosidade, SensorCO2
- **Polimorfismo**: Método `_gerar_valor()` implementado diferentemente em cada classe

### Tratamento de Exceções
- Validação de tipos e valores de entrada
- Tratamento específico para diferentes tipos de erro
- Mensagens de erro informativas para o usuário
- Recuperação graceful de erros

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
├── main.py              # Interface principal com tratamento de exceções
├── sensor.py            # Hierarquia de classes com herança e polimorfismo
│   ├── SensorBase       # Classe abstrata base
│   ├── SensorTemperatura
│   ├── SensorUmidade
│   ├── SensorPressao
│   ├── SensorLuminosidade
│   ├── SensorCO2
│   └── GerenciadorSensores
├── armazenamento.py     # Classe ArmazenamentoDados com validações
├── relatorio.py         # Classe GeradorRelatorio com estatísticas
├── dados_sensores.json  # Arquivo de dados (gerado automaticamente)
└── README.md           # Este arquivo
```

## Critérios de Avaliação Atendidos

✅ **Organização do código**: Estrutura modular com separação clara de responsabilidades
✅ **Classes implementadas corretamente**: Classes bem definidas com encapsulamento adequado
✅ **Herança e Polimorfismo**: Hierarquia de sensores com classe base abstrata
✅ **Relatório gerado corretamente**: Relatórios individuais e completos com estatísticas
✅ **Tratamento de exceções**: Validações robustas e tratamento específico de erros

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
from sensor import GerenciadorSensores, SensorTemperatura
from armazenamento import ArmazenamentoDados

# Criar instâncias
gerenciador = GerenciadorSensores()
armazenamento = ArmazenamentoDados()

# Coletar leitura (com tratamento de exceções)
try:
    leitura = gerenciador.coletar_leitura(1)  # Sensor de temperatura
    armazenamento.salvar_leitura(leitura)
    print("Leitura salva com sucesso!")
except ValueError as e:
    print(f"Erro de validação: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")

# Usar sensor específico diretamente
sensor_temp = SensorTemperatura(1)
leitura = sensor_temp.coletar_leitura()
```

## Formato dos Dados

```json
{
  "sensor_id": 1,
  "tipo": "Temperatura",
  "valor": 23.5,
  "timestamp": "2024-01-15 14:30:25 UTC"
}
```

## Funcionalidades Avançadas

- **Estatísticas**: Cálculo automático de média, mínimo, máximo e total de leituras
- **Validações**: Verificação de tipos, valores e existência de sensores
- **Timezone**: Timestamps em UTC para consistência
- **Recuperação de Erros**: Sistema continua funcionando mesmo com erros pontuais