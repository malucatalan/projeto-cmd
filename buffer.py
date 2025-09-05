from prompt_toolkit import prompt
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings

#IMPORTANTE: checar se essabiblioteca terá conflito com os.system

atalhos = KeyBindings() 
i = 0
historico = [1,2,3,4,5]

@atalhos.add("up") #a função _main não precisa ser importada em nenhum momento do código.. 
#pois o @ simboliza que a função seguinte é seu 'acompanhamento'

def _main(event): #underline é uma convenção que eu não entendi direito ainda
    #renomear esta função, falar com a Isa primeiro
    def buffer():

        global i

        if i == len(historico):
            i = 0

        print(historico[0+i])
        i += 1

    run_in_terminal(buffer)


text = prompt("GIM> ", key_bindings=atalhos)
print(f"You said: {text}")

