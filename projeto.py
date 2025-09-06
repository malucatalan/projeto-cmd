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

        # volta diretório
        if comando == "cd ..":
            os.chdir('..')
            diretorioAtual = os.getcwd()
            HistoricoArray.append(comando)
            print(HistoricoArray)

        # lista diretórios
        elif comando == "dir".strip():
            HistoricoArray.append(comando)
            for item in itensDiretorio:
                print(item)
            print(HistoricoArray)

        # muda diretorio para outro específico
        elif comando.startswith("cd "): 
            novoDiretorio = comando[3:].strip()

            try:
                os.chdir(novoDiretorio)
                diretorioAtual = os.getcwd()
                HistoricoArray.append(comando)
                print(HistoricoArray)

            except:
                print(f"Diretório não encontrado: {novoDiretorio}")

        elif comando == os.system(comando):
            os.system(comando)
            HistoricoArray.append(comando)
            print(HistoricoArray)
        
        else:
            print("Comando não encontrado.")
        
        # sair
        if comando in ['sair', 'quit']:
            print("Fim da execução do shell G.I.M")
            break

def buffer():

    global i

    if i == len(HistoricoArray):
        i = 0

    print(HistoricoArray[0+i])
    i += 1

    run_in_terminal(buffer)

main()
