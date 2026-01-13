from typing import List
from sensor import GerenciadorSensores
from armazenamento import ArmazenamentoDados

# Classe responsável por gerar e exibir relatórios dos sensores
class GeradorRelatorio:
    def __init__(self, gerenciador: GerenciadorSensores, armazenamento: ArmazenamentoDados):
        self.gerenciador = gerenciador  # Referência ao gerenciador de sensores
        self.armazenamento = armazenamento  # Referência ao armazenamento
    
    def mostrar_leituras(self, sensor_id: int):
        # Obtém leituras do arquivo JSON
        leituras = self.armazenamento.obter_leituras_por_sensor(sensor_id)
        
        # Verifica se existem leituras
        if not leituras:
            print("Nenhuma leitura encontrada.")
            return
        
        # Obtém o tipo do sensor para exibir no cabeçalho
        tipo = self.gerenciador.sensores[sensor_id].tipo
        print(f"\n=== LEITURAS - {tipo.upper()} ===")
        
        # Exibe as últimas 10 leituras
        for leitura in leituras[-10:]:
            print(f"Valor: {leitura['valor']} | {leitura['timestamp']}")
    
    def mostrar_relatorio_completo(self):
        # Exibe relatório de todos os sensores
        print("\n=== RELATÓRIO COMPLETO - TODOS OS SENSORES ===")
        
        # Loop pelos 5 sensores
        for sensor_id in range(1, 6):
            leituras = self.armazenamento.obter_leituras_por_sensor(sensor_id)
            
            if leituras:
                tipo = self.gerenciador.sensores[sensor_id].tipo
                print(f"\n--- {tipo.upper()} ---")
                
                # Mostra últimas 5 leituras de cada sensor
                for leitura in leituras[-5:]:
                    print(f"  Valor: {leitura['valor']} | {leitura['timestamp']}")
            else:
                tipo = self.gerenciador.sensores[sensor_id].tipo
                print(f"\n--- {tipo.upper()} ---")
                print("  Nenhuma leitura encontrada.")