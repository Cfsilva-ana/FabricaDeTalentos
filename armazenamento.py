import json
from typing import Dict, List
import os

# Classe responsável por salvar e carregar dados em arquivo JSON
class ArmazenamentoDados:
    def __init__(self, arquivo: str = "dados_sensores.json"):
        if not isinstance(arquivo, str) or not arquivo.strip():
            raise ValueError("Nome do arquivo deve ser uma string não vazia")
        self.arquivo = arquivo
    
    def salvar_leitura(self, leitura: Dict):
        if not isinstance(leitura, dict):
            raise TypeError("Leitura deve ser um dicionário")
        
        # Valida campos obrigatórios
        campos_obrigatorios = ['sensor_id', 'tipo', 'valor', 'timestamp']
        for campo in campos_obrigatorios:
            if campo not in leitura:
                raise ValueError(f"Campo obrigatório '{campo}' não encontrado na leitura")
        
        try:
            # Carrega dados existentes
            dados = self._carregar_dados_existentes()
            
            # Adiciona a nova leitura
            dados.append(leitura)
            
            # Salva os dados atualizados
            self._salvar_dados(dados)
            
        except Exception as e:
            raise RuntimeError(f"Erro ao salvar leitura: {e}")
    
    def _carregar_dados_existentes(self) -> List[Dict]:
        """Método auxiliar para carregar dados existentes do arquivo"""
        try:
            if not os.path.exists(self.arquivo):
                return []
                
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    return []
                
                dados = json.loads(content)
                
                # Validação de tipo
                if not isinstance(dados, list):
                    print(f"Aviso: Arquivo {self.arquivo} contém dados inválidos. Criando novo arquivo.")
                    return []
                
                return dados
                
        except json.JSONDecodeError as e:
            print(f"Aviso: Erro ao decodificar JSON em {self.arquivo}: {e}. Criando novo arquivo.")
            return []
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar dados existentes: {e}")
    
    def _salvar_dados(self, dados: List[Dict]):
        """Método auxiliar para salvar dados no arquivo"""
        try:
            with open(self.arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise RuntimeError(f"Erro ao salvar dados no arquivo: {e}")
    
    def carregar_leituras(self) -> List[Dict]:
        """Carrega todas as leituras do arquivo JSON"""
        try:
            dados = self._carregar_dados_existentes()
            return dados
        except Exception as e:
            print(f"Erro ao carregar leituras: {e}")
            return []
    
    def obter_leituras_por_sensor(self, sensor_id: int) -> List[Dict]:
        """Filtra leituras de um sensor específico"""
        if not isinstance(sensor_id, int):
            raise TypeError("ID do sensor deve ser um inteiro")
        
        try:
            todas_leituras = self.carregar_leituras()
            leituras_filtradas = [leitura for leitura in todas_leituras 
                                if leitura.get('sensor_id') == sensor_id]
            return leituras_filtradas
        except Exception as e:
            raise RuntimeError(f"Erro ao obter leituras do sensor {sensor_id}: {e}")
    
    def obter_estatisticas(self, sensor_id: int) -> Dict:
        """Retorna estatísticas básicas de um sensor"""
        try:
            leituras = self.obter_leituras_por_sensor(sensor_id)
            if not leituras:
                return {"total": 0, "media": 0, "minimo": 0, "maximo": 0}
            
            valores = [leitura['valor'] for leitura in leituras]
            return {
                "total": len(valores),
                "media": round(sum(valores) / len(valores), 2),
                "minimo": min(valores),
                "maximo": max(valores)
            }
        except Exception as e:
            raise RuntimeError(f"Erro ao calcular estatísticas do sensor {sensor_id}: {e}")