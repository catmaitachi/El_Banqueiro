import threading
import random
import time
import banqueiro

NUMERO_DE_CICLOS = 5

def _iniciar_rotina(cliente_id: int):

    for ciclo in range(NUMERO_DE_CICLOS):

        solicitacao = [random.randint(0, banqueiro.necessidade[cliente_id][j]) for j in range(banqueiro.NUMERO_DE_RECURSOS)]
        banqueiro.solicitar_recursos(cliente_id, solicitacao)

        time.sleep(random.uniform(0.1, 1.0))

        tem_algo_alocado = any(banqueiro.alocacao[cliente_id][j] > 0 for j in range(banqueiro.NUMERO_DE_RECURSOS))

        if tem_algo_alocado:

            liberacao = [random.randint(0, banqueiro.alocacao[cliente_id][j]) for j in range(banqueiro.NUMERO_DE_RECURSOS)]
            banqueiro.liberar_recursos(cliente_id, liberacao)

        time.sleep(random.uniform(0.05, 0.1))

    print(f"[ Cliente {cliente_id} ] 🎉 Todos os ciclos concluídos.")

def iniciar_clientes():

    thread = []

    for i in range(banqueiro.NUMERO_DE_CLIENTES):

        t = threading.Thread(target=_iniciar_rotina, args=(i,), name=f"Cliente-{i}")
        thread.append(t)

    for t in thread:
        t.start()

    for t in thread:
        t.join()



        