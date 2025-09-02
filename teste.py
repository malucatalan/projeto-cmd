def cmd ():

    hist_comandos = []

    while True:
        entrada = input("sei la o que escreve aqui> ")

        if entrada == "":
            continue

        elif entrada == "exit":
            print("Saindo...")
            break

        hist_comandos.append(entrada)

cmd()