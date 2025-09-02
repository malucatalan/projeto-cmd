def cmd ():

    while True:
        entrada = input("sei la o que escreve aqui> ")

        if entrada == "":
            continue

        elif entrada == "exit":
            print("Saindo...")
            break

cmd()