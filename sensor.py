import random
from datetime import datetime, timezone
from typing import List, Dict
from abc import ABC, abstractmethod

# Classe abstrata base para todos os sensores
class SensorBase(ABC):
    def __init__(self, sensor_id: int, tipo: str):
        if not isinstance(sensor_id, int) or sensor_id <= 0:
            raise ValueError("ID do sensor deve ser um inteiro positivo")
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("Tipo do sensor deve ser uma string não vazia")
            
        self.sensor_id = sensor_id
        self.tipo = tipo
        self.leituras = []
    
    @abstractmethod
    def _gerar_valor(self) -> float:
        """Método abstrato para gerar valor específico do sensor"""
        pass
    
    def coletar_leitura(self) -> Dict:
        try:
            valor = self._gerar_valor()
            leitura = {
                "sensor_id": self.sensor_id,
                "tipo": self.tipo,
                "valor": valor,
                "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            }
            self.leituras.append(leitura)
            return leitura
        except Exception as e:
            raise RuntimeError(f"Erro ao coletar leitura do sensor {self.sensor_id}: {e}")

# Classes específicas para cada tipo de sensor (Herança e Polimorfismo)
class SensorTemperatura(SensorBase):
    def __init__(self, sensor_id: int):
        super().__init__(sensor_id, "Temperatura")
    
    def _gerar_valor(self) -> float:
        return round(random.uniform(15, 35), 1)

class SensorUmidade(SensorBase):
    def __init__(self, sensor_id: int):
        super().__init__(sensor_id, "Umidade")
    
    def _gerar_valor(self) -> float:
        return round(random.uniform(30, 90), 1)

class SensorPressao(SensorBase):
    def __init__(self, sensor_id: int):
        super().__init__(sensor_id, "Pressao")
    
    def _gerar_valor(self) -> float:
        return round(random.uniform(980, 1030), 1)

class SensorLuminosidade(SensorBase):
    def __init__(self, sensor_id: int):
        super().__init__(sensor_id, "Luminosidade")
    
    def _gerar_valor(self) -> float:
        return round(random.uniform(0, 1000), 1)

class SensorCO2(SensorBase):
    def __init__(self, sensor_id: int):
        super().__init__(sensor_id, "CO2")
    
    def _gerar_valor(self) -> float:
        return round(random.uniform(300, 1000), 1)

# Classe que gerencia todos os sensores
class GerenciadorSensores:
    def __init__(self):
        self.sensores = {}          # Dicionário para armazenar os sensores
        self._inicializar_sensores() # Cria os 5 sensores automaticamente
    
    def _inicializar_sensores(self):
        # Cria sensores específicos usando herança
        try:
            self.sensores[1] = SensorTemperatura(1)
            self.sensores[2] = SensorUmidade(2)
            self.sensores[3] = SensorPressao(3)
            self.sensores[4] = SensorLuminosidade(4)
            self.sensores[5] = SensorCO2(5)
        except Exception as e:
            raise RuntimeError(f"Erro ao inicializar sensores: {e}")
    
    def coletar_leitura(self, sensor_id: int) -> Dict:
        # Validação do sensor_id
        if not isinstance(sensor_id, int):
            raise TypeError("ID do sensor deve ser um inteiro")
        if sensor_id not in self.sensores:
            raise ValueError(f"Sensor com ID {sensor_id} não encontrado. IDs válidos: {list(self.sensores.keys())}")
        
        try:
            return self.sensores[sensor_id].coletar_leitura()
        except Exception as e:
            raise RuntimeError(f"Erro ao coletar leitura do sensor {sensor_id}: {e}")
    
    def obter_leituras(self, sensor_id: int) -> List[Dict]:
        # Validação do sensor_id
        if not isinstance(sensor_id, int):
            raise TypeError("ID do sensor deve ser um inteiro")
        if sensor_id not in self.sensores:
            raise ValueError(f"Sensor com ID {sensor_id} não encontrado. IDs válidos: {list(self.sensores.keys())}")
        
        return self.sensores[sensor_id].leituras
    
    def obter_tipos(self) -> Dict[int, str]:
        # Retorna um dicionário com ID e tipo de cada sensor
        return {sensor_id: sensor.tipo for sensor_id, sensor in self.sensores.items()}
    
    def validar_sensor_id(self, sensor_id: int) -> bool:
        """Método auxiliar para validar se um sensor_id existe"""
        return isinstance(sensor_id, int) and sensor_id in self.sensores