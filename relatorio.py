from typing import List
from sensor import GerenciadorSensores
from armazenamento import ArmazenamentoDados

# Classe responsável por gerar e exibir relatórios dos sensores
class GeradorRelatorio:
    def __init__(self, gerenciador: GerenciadorSensores, armazenamento: ArmazenamentoDados):
        if not isinstance(gerenciador, GerenciadorSensores):
            raise TypeError("Gerenciador deve ser uma instância de GerenciadorSensores")
        if not isinstance(armazenamento, ArmazenamentoDados):
            raise TypeError("Armazenamento deve ser uma instância de ArmazenamentoDados")
            
        self.gerenciador = gerenciador
        self.armazenamento = armazenamento
    
    def mostrar_leituras(self, sensor_id: int):
        """Exibe leituras de um sensor específico"""
        try:
            # Validação do sensor_id
            if not self.gerenciador.validar_sensor_id(sensor_id):
                print(f"Erro: Sensor com ID {sensor_id} não encontrado.")
                return
            
            # Obtém leituras do arquivo JSON
            leituras = self.armazenamento.obter_leituras_por_sensor(sensor_id)
            
            # Verifica se existem leituras
            if not leituras:
                print("Nenhuma leitura encontrada.")
                return
            
            # Obtém o tipo do sensor
            tipo = self.gerenciador.sensores[sensor_id].tipo
            print(f"\n=== LEITURAS - {tipo.upper()} ===")
            
            # Exibe as últimas 10 leituras
            for leitura in leituras[-10:]:
                print(f"Valor: {leitura['valor']} | {leitura['timestamp']}")
            
            # Exibe estatísticas
            self._mostrar_estatisticas(sensor_id)
            
        except Exception as e:
            print(f"Erro ao mostrar leituras do sensor {sensor_id}: {e}")
    
    def _mostrar_estatisticas(self, sensor_id: int):
        """Método auxiliar para exibir estatísticas de um sensor"""
        try:
            stats = self.armazenamento.obter_estatisticas(sensor_id)
            if stats['total'] > 0:
                print(f"\n--- ESTATÍSTICAS ---")
                print(f"Total de leituras: {stats['total']}")
                print(f"Média: {stats['media']}")
                print(f"Mínimo: {stats['minimo']}")
                print(f"Máximo: {stats['maximo']}")
        except Exception as e:
            print(f"Erro ao calcular estatísticas: {e}")
    
    def mostrar_relatorio_completo(self):
        """Exibe relatório de todos os sensores"""
        try:
            print("\n=== RELATÓRIO COMPLETO - TODOS OS SENSORES ===")
            
            # Loop pelos 5 sensores
            for sensor_id in range(1, 6):
                try:
                    leituras = self.armazenamento.obter_leituras_por_sensor(sensor_id)
                    tipo = self.gerenciador.sensores[sensor_id].tipo
                    
                    print(f"\n--- {tipo.upper()} ---")
                    
                    if leituras:
                        # Mostra últimas 5 leituras de cada sensor
                        for leitura in leituras[-5:]:
                            print(f"  Valor: {leitura['valor']} | {leitura['timestamp']}")
                        
                        # Mostra estatísticas resumidas
                        stats = self.armazenamento.obter_estatisticas(sensor_id)
                        if stats['total'] > 0:
                            print(f"  Total: {stats['total']} | Média: {stats['media']}")
                    else:
                        print("  Nenhuma leitura encontrada.")
                        
                except Exception as e:
                    print(f"  Erro ao processar sensor {sensor_id}: {e}")
                    
        except Exception as e:
            print(f"Erro ao gerar relatório completo: {e}")