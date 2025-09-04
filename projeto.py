'''Os passos a serem inicialmente implementados são:
 (1) desmembrar (parse) a entrada para obter o comando e seus parâmetros
 (2) criar um objeto ProcessBuilder
 (3) iniciar o processo
 (4) obter o fluxo de saída
 (5) enviar o conteúdo retornado pelo comando'''

import os
import subprocess

# Cria uma função main onde:
def main():

    # Diretório atual é atribuído para uma variável.
    diretorioAtual = os.getcwd()

# Entra em um looping para repetir a entrada de comando até o usuário mandar o programar parar 
    while True:

        itensDiretorio = os.listdir(diretorioAtual)

    # Aqui, ele cria uma variável para pegar o comando em caixa baixa do usuário, para que ele possa realizar outros processos, como a navegação e o subprocess.    
        comando = input(f'\nGIM {diretorioAtual}>> ').lower().strip()

        if comando == "" or comando == "cd.".strip():
            continue

    # Lista todas as pastas do diretório atual
        elif comando == "dir".strip():
            print("O volume na unidade C não tem nome.")
            print("O Número de Série do Volume é não sei ainda como faz\n")
            for item in itensDiretorio:
                print(item)

      # Só printa o repositório atual e não muda mais nada
        elif comando == "cd".strip():
            print(diretorioAtual)
        
    # Volta para o repositório anterior do atual
        elif comando == "cd..":
            os.chdir("..")
            diretorioAtual = os.getcwd()
        
    #Troca o diretório para a pasta que o usuário digitou
        elif comando.startswith("cd "): 
            novoDiretorio = comando[3:]
            os.chdir(novoDiretorio)
            diretorioAtual = os.getcwd()

    # Caso o comando for "Sair", ele acabará a repetição.    
        elif comando == "sair".lower():
            print("Saindo...")
            break
    
    # !!!!!!!!!!! Importante>>>>>> Aqui ele precisaria de uma condição para navegar no diretório através da biblioteca OS. 
    # Tipo, se você rodar ele agora, ele só vai listar o diretório atual, que no meu caso é a pasta do Visual Code. Então é preciso manipulação de diretório aqui!

    # Creio eu que o buffer poderia ser chamado após essa estrutura de navegação.
    

    # Aqui, ele pega a função parse e exibe no terminal. Só para mostrar que a lista foi feita.
        else:
            parse(comando)
            resultado = parse(comando)
            print(resultado)


# Essa função retorna o comando em formato de lista: ["tipo", "assim"]
def parse(comando: str):
    comandoLista = comando.split()
    return comandoLista

# Essa função puxa o comandoLista e realiza o Subprocess/ProcessBuilder, onde ele vai observar o primeiro item da lista como um comando e os próximos itens do comandoLista como parâmetros.
def execucaoComando(comandoLista):
    try:
        processo = subprocess.Popen(comandoLista, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
    except FileNotFoundError:
        return "O comando não foi encontrado."

    # O comando try vai tentar (avá) criar um subprocesso (Subprocesso é um processo do sistema) a partir dos seguintes argumentos: A lista de comandos, a saída (que recebe .PIPE = onde permite o redirecionamento de uma resposta 
    # para outra entrada, e stderr mescla mensagens de erro (como quando a gente testa e dá o erro em vermelho), junto do stdout. Ou seja, todo comando, seja ele certo ou errado, vai pro mesmo lugar.)
    # Se o comando não for encontrado, não vai funcionar.


    # Aqui, ele lê a captura do processo que fizemos e através do .communicate, espera o código terminar. Porém, se o comando demorar mais de 10 segundos para rodar, ele faz .kill(), que 
    # intervém e "mata" o processo.

    try:
        out, _ = processo.communicate(timeout=10)

    except subprocess.TimeoutExpired:
        processo.kill()
        # aqui ele recebe a saída de out, esse _ ignora outra saída. 
        out, _ = processo.communicate()
        out = out + "Processo não finalizado no tempo."
    
    return out


main()
