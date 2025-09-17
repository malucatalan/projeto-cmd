import os

HistoricoArray = []
i = len(HistoricoArray)
# cria uma função para o buffer
def buffer(comando,HistoricoArray):

        try:
            if comando == '!!':

                # avisa o usuário se o histórico estiver vazio
                if not HistoricoArray:
                    print('Histórico de comandos vazio.')
                    return None
                
                # cria uma variável para o comando anterior que foi salvo na histórico
                comando_historico = HistoricoArray[-1]
                HistoricoArray.append(comando)
            
            else: 
                # verifica com o índice utilizado para chamar o comando
                indice = int(comando[1:])
                comando_historico = HistoricoArray[indice]
                HistoricoArray.append(comando)

            return comando_historico

        except (ValueError,IndexError):
            print(f"'{comando}' não é um comando válido")

# Cria uma função main onde:
def main():

    # Diretório atual é atribuído para uma variável.
    diretorioAtual = os.getcwd()

    # Entra em um looping para repetir a entrada de comando até o usuário mandar o programar parar 
    while True:
        itensDiretorio = os.listdir()
        
        # Aqui, ele cria uma variável para pegar o comando em caixa baixa do usuário, para que ele possa realizar outros processos, como a navegação e o subprocess.    
        comando = input(f'\nGIM {diretorioAtual}>> ').lower().strip()

        if comando == "":
            continue
        
        # executa novamente o comando que está no histórico 
        if comando.startswith('!!') or (comando.startswith('!') and len(comando) > 1):
            rodar_historico = buffer(comando, HistoricoArray)
            if rodar_historico:
                print(f'Executando comando: {rodar_historico}')
                comando = rodar_historico

        if comando.startswith('cd ') or comando.startswith('open '):
            if comando.startswith("cd "): 
                novoDiretorio = comando[3:].strip()

                try:
                    os.chdir(novoDiretorio)
                    diretorioAtual = os.getcwd()
                    HistoricoArray.append(comando)

                except:
                    print(f"Diretório não encontrado: {novoDiretorio}")
            
            # abre o aplicativo indicado
            else: 
                comando_open = comando[5:].strip()

                HistoricoArray.append(comando)
                os.system(comando_open)

        elif comando in ['dir', 'cd ..', 'history', 'task', 'exit', '!!']:
            if comando == 'task':
                print("DIR                             Lista todos os itens no diretório atual.")
                print("CD <DIRETORIO>                  Muda para o diretório especificado.")
                print("CD ..                           Volta para o diretório anterior.")
                print("HISTORY                         Mostra o histórico de comandos.")
                print("TASK                            Mostra esta lista de comandos.")
                print("OPEN <APLICATIVO>               Abre o aplicativo especificado.")
                print("!!                              Volta para o comando anterior.")
                print("!i                              Volta para o comando com o índice i indicado.")
                print("EXIT                            Finaliza o shell G.I.M.")
                HistoricoArray.append(comando)

            # lista o histórico de comandos chamados
            elif comando in ['history']:
                for c, item in enumerate(HistoricoArray):
                    print(f'[{c}] {item}')
                HistoricoArray.append(comando)

            # volta diretório
            elif comando == "cd ..":
                os.chdir('..')
                diretorioAtual = os.getcwd()
                HistoricoArray.append(comando)

            # lista diretórios
            elif comando == "dir".strip():
                HistoricoArray.append(comando)
                for item in itensDiretorio:
                    print(item)

            # sair 
            elif comando in ['exit']:
                print("Fim da execução do shell G.I.M")
                break

            else:
                print(f"'{comando}' não é um comando válido")
                HistoricoArray.append(comando)
        else:
            os.system(comando)

main()

