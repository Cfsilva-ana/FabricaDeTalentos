from sensor import GerenciadorSensores
from armazenamento import ArmazenamentoDados
from relatorio import GeradorRelatorio

def gerar_informacoes(gerenciador, armazenamento):
    """Gera leituras para todos os sensores"""
    try:
        print("\nGerando leituras para todos os sensores...")
        total_leituras = 0
        
        for sensor_id in range(1, 6):
            try:
                for _ in range(3):  # 3 leituras por sensor
                    leitura = gerenciador.coletar_leitura(sensor_id)
                    armazenamento.salvar_leitura(leitura)
                    total_leituras += 1
            except Exception as e:
                print(f"Erro ao gerar leituras do sensor {sensor_id}: {e}")
                
        print(f"Leituras geradas e salvas com sucesso! Total: {total_leituras}")
        
    except Exception as e:
        print(f"Erro geral ao gerar informações: {e}")

def menu_inicial():
    """Exibe o menu inicial e retorna a opção escolhida"""
    print("\n=== SISTEMA DE SENSORES ===")
    print("1 - Gerar informações")
    print("2 - Visualizar relatórios")
    print("3 - Sair")
    return input("Escolha uma opção: ")

def menu_relatorios():
    """Exibe o menu de relatórios e retorna a opção escolhida"""
    print("\n=== RELATÓRIOS ===")
    print("1 - Temperatura")
    print("2 - Umidade")
    print("3 - Pressão")
    print("4 - Luminosidade")
    print("5 - CO2")
    print("6 - Relatório completo")
    print("7 - Voltar")
    return input("Escolha um sensor: ")

def main():
    """Função principal do sistema"""
    try:
        # Inicialização dos componentes
        gerenciador = GerenciadorSensores()
        armazenamento = ArmazenamentoDados()
        relatorio = GeradorRelatorio(gerenciador, armazenamento)
        
        print("Sistema de Sensores iniciado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao inicializar o sistema: {e}")
        return
    
    # Loop principal
    while True:
        try:
            opcao = menu_inicial()
            
            if opcao == '1':
                gerar_informacoes(gerenciador, armazenamento)
                
            elif opcao == '2':
                _processar_menu_relatorios(relatorio)
                        
            elif opcao == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Escolha uma opção de 1 a 3.")
                
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        except ValueError as e:
            print(f"Erro de entrada: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def _processar_menu_relatorios(relatorio):
    """Processa o menu de relatórios"""
    while True:
        try:
            sensor_opcao = menu_relatorios()
            
            if sensor_opcao in ['1', '2', '3', '4', '5']:
                sensor_id = int(sensor_opcao)
                relatorio.mostrar_leituras(sensor_id)
            elif sensor_opcao == '6':
                relatorio.mostrar_relatorio_completo()
            elif sensor_opcao == '7':
                break
            else:
                print("Opção inválida! Escolha uma opção de 1 a 7.")
                
        except ValueError as e:
            print(f"Erro de entrada: {e}")
        except Exception as e:
            print(f"Erro ao processar relatório: {e}")

if __name__ == "__main__":
    main()