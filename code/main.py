import random
import cliente
import banqueiro

def _inicializar():

    for i in range(banqueiro.NUMERO_DE_RECURSOS):

        banqueiro.disponivel[i] = random.randint(1, 10)

    for i in range(banqueiro.NUMERO_DE_CLIENTES):

        for j in range(banqueiro.NUMERO_DE_RECURSOS):

            banqueiro.maximo[i][j] = random.randint(1, banqueiro.disponivel[j])
            banqueiro.necessidade[i][j] = banqueiro.maximo[i][j]

    print("Incializando...")

    for i, j in enumerate(banqueiro.maximo):

        print(f"[ Cliente {i} ] ⚙️ Máximo: {j} ")

if __name__ == "__main__":

    _inicializar()
    cliente.iniciar_clientes()