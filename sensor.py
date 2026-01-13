import random
from datetime import datetime
from typing import List, Dict

# Classe que representa um sensor individual
class Sensor:
    def __init__(self, sensor_id: int, tipo: str):
        self.sensor_id = sensor_id  # ID único do sensor
        self.tipo = tipo           # Tipo do sensor (Temperatura, Umidade, etc.)
        self.leituras = []         # Lista para armazenar todas as leituras
    
    def coletar_leitura(self) -> Dict:
        # Gera valores aleatórios baseados no tipo do sensor
        if self.tipo == "Temperatura":
            valor = round(random.uniform(15, 35), 1)      # 15°C a 35°C
        elif self.tipo == "Umidade":
            valor = round(random.uniform(30, 90), 1)      # 30% a 90%
        elif self.tipo == "Pressao":
            valor = round(random.uniform(980, 1030), 1)   # 980 a 1030 hPa
        elif self.tipo == "Luminosidade":
            valor = round(random.uniform(0, 1000), 1)     # 0 a 1000 lux
        elif self.tipo == "CO2":
            valor = round(random.uniform(300, 1000), 1)   # 300 a 1000 ppm
        
        # Cria o dicionário com os dados da leitura
        leitura = {
            "sensor_id": self.sensor_id,
            "tipo": self.tipo,
            "valor": valor,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Adiciona a leitura à lista interna e retorna
        self.leituras.append(leitura)
        return leitura

# Classe que gerencia todos os sensores
class GerenciadorSensores:
    def __init__(self):
        self.sensores = {}          # Dicionário para armazenar os sensores
        self._inicializar_sensores() # Cria os 5 sensores automaticamente
    
    def _inicializar_sensores(self):
        # Lista com os 5 tipos de sensores
        tipos = ["Temperatura", "Umidade", "Pressao", "Luminosidade", "CO2"]
        # Cria um sensor para cada tipo (IDs de 1 a 5)
        for i, tipo in enumerate(tipos, 1):
            self.sensores[i] = Sensor(i, tipo)
    
    def coletar_leitura(self, sensor_id: int) -> Dict:
        # Coleta uma leitura do sensor especificado
        return self.sensores[sensor_id].coletar_leitura()
    
    def obter_leituras(self, sensor_id: int) -> List[Dict]:
        # Retorna todas as leituras de um sensor específico
        return self.sensores[sensor_id].leituras
    
    def obter_tipos(self) -> Dict[int, str]:
        # Retorna um dicionário com ID e tipo de cada sensor
        return {id: sensor.tipo for id, sensor in self.sensores.items()}