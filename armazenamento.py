import json
from typing import Dict, List

# Classe responsável por salvar e carregar dados em arquivo JSON
class ArmazenamentoDados:
    def __init__(self, arquivo: str = "dados_sensores.json"):
        self.arquivo = arquivo  # Nome do arquivo onde os dados serão salvos
    
    def salvar_leitura(self, leitura: Dict):
        # Tenta carregar dados existentes do arquivo
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                content = f.read().strip()  # Lê o conteúdo e remove espaços
                if content:
                    dados = json.loads(content)  # Converte JSON para lista Python
                    # Verifica se os dados são uma lista, senão cria nova lista
                    if not isinstance(dados, list):
                        dados = []
                else:
                    dados = []  # Arquivo vazio, cria lista nova
        except (FileNotFoundError, json.JSONDecodeError):
            # Se arquivo não existe ou JSON inválido, cria lista nova
            dados = []
        
        # Adiciona a nova leitura à lista
        dados.append(leitura)
        
        # Salva a lista atualizada no arquivo JSON
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
    
    def carregar_leituras(self) -> List[Dict]:
        # Carrega todas as leituras do arquivo JSON
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def obter_leituras_por_sensor(self, sensor_id: int) -> List[Dict]:
        # Filtra leituras de um sensor específico
        todas_leituras = self.carregar_leituras()
        return [leitura for leitura in todas_leituras if leitura.get('sensor_id') == sensor_id]