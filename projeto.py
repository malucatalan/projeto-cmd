import os
from prompt_toolkit import prompt
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings

HistoricoArray = []
atalhos = KeyBindings() 
i = 0
@atalhos.add("up")

# Cria uma função main onde:
def main():

    run_in_terminal(buffer)
    # Diretório atual é atribuído para uma variável.
    diretorioAtual = os.getcwd()

# Entra em um looping para repetir a entrada de comando até o usuário mandar o programar parar 
    while True:
        itensDiretorio = os.listdir()
    # Aqui, ele cria uma variável para pegar o comando em caixa baixa do usuário, para que ele possa realizar outros processos, como a navegação e o subprocess.    
        comando = input(f'\nGIM {diretorioAtual}>> ').lower().strip()
        
        # ignora
        if comando == "":
            continue

        elif comando == 'task':
            print("DIR                             Lista todos os itens no diretório atual.")
            print("CD <DIRETORIO>                  Muda para o diretório especificado.")
            print("CD ..                           Volta para o diretório anterior.")
            print("HISTORY                         Mostra o histórico de comandos.")
            print("TASKS                           Mostra esta lista de comandos.")
            print("EXIT                            Finaliza o shell G.I.M.")
            HistoricoArray.append(comando)

        # lista o histórico de comandos chamados
        elif comando in ['history']:
            for item in HistoricoArray:
                print(item)

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

        # muda diretorio para outro específico
        elif comando.startswith("cd "): 
            novoDiretorio = comando[3:].strip()

            try:
                os.chdir(novoDiretorio)
                diretorioAtual = os.getcwd()
                HistoricoArray.append(comando)

            except:
                print(f"Diretório não encontrado: {novoDiretorio}")

        # sair 
        elif comando in ['exit']:
            print("Fim da execução do shell G.I.M")
            break

        # condição de erro para comandos inválidos
        else:
            print(f"'{comando}' não é um comando válido")
            HistoricoArray.append(comando)

    # criar a função buffer onde:
    def buffer():

        # acessa a variável global i
        global i

        if i == len(HistoricoArray):
            i = 0

        # printa o comando atual
        print(HistoricoArray[0+i])
        i += 1

        run_in_terminal(buffer)

    # inicia o programa chamando a função main
    main()
