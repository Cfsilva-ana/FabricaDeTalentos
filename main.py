from sensor import GerenciadorSensores
from armazenamento import ArmazenamentoDados
from relatorio import GeradorRelatorio

def gerar_informacoes(gerenciador, armazenamento):
    print("\nGerando leituras para todos os sensores...")
    for sensor_id in range(1, 6):
        for _ in range(3):  # 3 leituras por sensor cada sensor
            leitura = gerenciador.coletar_leitura(sensor_id)
            armazenamento.salvar_leitura(leitura)
    print("Leituras geradas e salvas com sucesso!")

def menu_inicial(): #Opções do menu inicial
    print("\n=== SISTEMA DE SENSORES ===")
    print("1 - Gerar informações")
    print("2 - Visualizar relatórios")
    print("3 - Sair")
    return input("Escolha uma opção: ") #Fecha o programa

def menu_relatorios(): 
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
    gerenciador = GerenciadorSensores()
    armazenamento = ArmazenamentoDados()
    relatorio = GeradorRelatorio(gerenciador, armazenamento)
    
    while True:
        try:
            opcao = menu_inicial()
            
            if opcao == '1':
                gerar_informacoes(gerenciador, armazenamento)
                
            elif opcao == '2':
                while True:
                    sensor_opcao = menu_relatorios()
                    
                    if sensor_opcao in ['1', '2', '3', '4', '5']:
                        sensor_id = int(sensor_opcao)
                        relatorio.mostrar_leituras(sensor_id)
                    elif sensor_opcao == '6':
                        relatorio.mostrar_relatorio_completo()
                    elif sensor_opcao == '7':
                        break
                    else:
                        print("Opção inválida!")
                        
            elif opcao == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
                
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()