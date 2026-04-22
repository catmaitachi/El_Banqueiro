import threading

NUMERO_DE_CLIENTES = 5
NUMERO_DE_RECURSOS = 3

disponivel  =  [0] * NUMERO_DE_RECURSOS
maximo      = [[0] * NUMERO_DE_RECURSOS for _ in range(NUMERO_DE_CLIENTES)]
alocacao    = [[0] * NUMERO_DE_RECURSOS for _ in range(NUMERO_DE_CLIENTES)]
necessidade = [[0] * NUMERO_DE_RECURSOS for _ in range(NUMERO_DE_CLIENTES)]

lock = threading.Lock()

def _eh_seguro() -> bool:

    clientes_simulados  = [False] * NUMERO_DE_CLIENTES
    disponivel_copia    = disponivel[:]
    simulacao_ok        = True

    while simulacao_ok:

        simulacao_ok = False

        for i in range(NUMERO_DE_CLIENTES):

            if clientes_simulados[i]: continue

            eh_suficiente = all(necessidade[i][j] <= disponivel_copia[j] for j in range(NUMERO_DE_RECURSOS))

            if eh_suficiente:

                for j in range(NUMERO_DE_RECURSOS):
                    
                    disponivel_copia[j] += alocacao[i][j]

                clientes_simulados[i] = True
                simulacao_ok = True
    
    return all(clientes_simulados)

def solicitar_recursos(cliente_id: int, solicitacao: list) -> int:
    
    with lock:

        print(f"[ Cliente {cliente_id} ] 🫴 Solicitando: {solicitacao}")

        for j in range(NUMERO_DE_RECURSOS):

            if solicitacao[j] > necessidade[cliente_id][j]:

                print(f"[ Cliente {cliente_id} ] ❌ Negado: Solicitação excessiva.")
                return -1

            if solicitacao[j] > disponivel[j]:

                print(f"[ Cliente {cliente_id} ] ❌ Negado: Recursos insuficientes.")
                return -1
            
        for j in range(NUMERO_DE_RECURSOS):

            disponivel[j]               -= solicitacao[j]
            alocacao[cliente_id][j]     += solicitacao[j]
            necessidade[cliente_id][j]  -= solicitacao[j]

        if _eh_seguro():

            print(f"[ Cliente {cliente_id} ] ✅ Aprovado: Recursos alocados.")
            return 0
        
        else:

            for j in range(NUMERO_DE_RECURSOS):

                disponivel[j]               += solicitacao[j]
                alocacao[cliente_id][j]     -= solicitacao[j]
                necessidade[cliente_id][j]  += solicitacao[j]

            print(f"[ Cliente {cliente_id} ] ❌ Negado: Estado inseguro.")
            return -1
        
def liberar_recursos(cliente_id: int, liberacao: list) -> int:

    with lock:

        print(f"[ Cliente {cliente_id} ] 👍 Liberando: {liberacao}")

        for j in range(NUMERO_DE_RECURSOS):

            if liberacao[j] > alocacao[cliente_id][j]:

                print(f"[ Cliente {cliente_id} ] ❌ Negado: Liberação excessiva.")
                return -1
            
        for j in range(NUMERO_DE_RECURSOS):

            disponivel[j]               += liberacao[j]
            alocacao[cliente_id][j]     -= liberacao[j]
            necessidade[cliente_id][j]  += liberacao[j]
        
        print(f"[ Cliente {cliente_id} ] ✅ Aprovado: Recursos liberados.")
        return 0
        