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
    print("-"*50)
    print("𝔼𝕩𝕡𝕝𝕠𝕣𝕒𝕕𝕠𝕣 𝕕𝕖 𝔸𝕣𝕢𝕦𝕚𝕧𝕠𝕤")
    print("-"*50)

    # Diretório atual é atribuído para uma variável.
    diretorioAtual = os.getcwd()

    # Entra em uma estrutura de repetição que mostra o diretório e os itens dentro desse diretório, enumerando-os com um For (onde o i é o contador, item é o item dentro do diretório e o parâmetro 
    # ENUMERATE cria um contador automático onde, a partir do número 1, enumera itens de dentro da variável ItensDiretório.)
    while True:
        print("Você está nesse diretório: ", diretorioAtual)
        itensDiretorio = os.listdir(diretorioAtual)

        for i, item in enumerate(itensDiretorio, start= 1):
            print(i,".", item)

    # Aqui, ele cria uma variável para pegar o comando em caixa baixa do usuário, para que ele possa realizar outros processos, como a navegação e o subprocess.    
        comando = input("GIM>> ").lower()

    # Caso o comando for "Sair", ele acabará a repetição.    
        if comando == "sair":
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
