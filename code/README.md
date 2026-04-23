# Algoritmo do Banqueiro - Código 

###  Estrutura de arquivos

```

    📂 El_Banqueiro/
    ├──💻 code/
    │  ├── banqueiro.py  # Lógica de controle de recursos
    │  ├── cliente.py    # Simulação de clientes
    │  └── main.py       # Inicialização 
    └──📄 docs/

```

## 🏦 O Banqueiro

`banqueiro.py` contém os **dados globais** compartilhados entre os clientes e as **funções principais** do algoritmo.

---

### Estruturas de dados

| Variável | Tipo | Descrição |
|---|---|---|
| `disponivel` | `list[int]` | Quantidade disponível de cada recurso no momento |
| `maximo` | `list[list[int]]` | Demanda máxima de cada cliente por recurso |
| `alocacao` | `list[list[int]]` | Quanto cada cliente tem alocado atualmente |
| `necessidade` | `list[list[int]]` | Valor prévio da quantidade de recursos que cada cliente pode precisar |
| `lock` | `threading.Lock` | Mutex que protege o acesso concorrente às estruturas acima |

---

### Algoritmo de segurança

`eh_seguro()` Verifica se o estado atual do sistema é seguro, ou seja, se existe ao menos uma sequência em que todos os clientes conseguem terminar.

**Como funciona:**

1. Cria uma cópia local de `disponivel` para simular sem alterar o estado real.
2. Marca todos os clientes como `não simulados`.
3. Em loop, procura um cliente cujas necessidades possam ser atendidas.
4. Quando encontra, simula que ele terminou e devolve seus recursos a copia local de `disponivel`.
5. Repete até não encontrar mais nenhum cliente elegível
6. Se todos foram finalizados o estado seguro (`True`); caso contrário é inseguro (`False`)

---

### Solicitação de recursos

`solicitar_recursos()` processa uma solicitação de recursos de um cliente. Retorna `0` se aprovada, `-1` se negada.

**Verificações realizadas em ordem:**
 
1. **Pedido dentro da necessidade** — o cliente não pode pedir mais do que declarou precisar
2. **Recursos disponíveis** — o pedido não pode exceder o que está disponível no momento
3. **Estado seguro após alocação** — realiza uma simulação e chama `eh_seguro()`; se o resultado for inseguro, faz **rollback** completo e nega o pedido.

Todo o bloco é executado dentro do `lock` para evitar condições de corrida.

---
 
### Liberação de recursos
 
`liberar_recursos()` processa a devolução de recursos por um cliente. Retorna `0` se bem-sucedida, `-1` em caso de erro.
 
**Funcionamento:**
1. Verifica se o cliente não está tentando liberar mais do que possui alocado
2. Atualiza `disponivel`, `alocacao` e `necessidade` de forma consistente
3. Libera o recurso.

Também executado dentro do `lock`.
 
---

## 🤖 Os Clientes
 
`cliente.py` define a **lógica de cada thread de cliente** e a função que cria e gerencia todas as threads.

---
 
### Rotina dos clientes
 
`_rotina()` é a função executada por cada thread. Roda um loop de `NUMERO_DE_CICLOS` iterações onde cada ciclo consiste em:
 
1. **Gerar solicitação aleatória** — valores entre `0` e `necessidade[i][j]` para cada recurso
2. **Solicitar ao banqueiro** — chama `solicitar_recursos()`; registra um log do resultado
3. **Simular uso dos recursos** — `time.sleep()` com duração aleatória
4. **Liberar recursos aleatoriamente** — se tiver algo alocado, devolve uma parte aleatória via `liberar_recursos()`
5. **Pequena pausa** antes do próximo ciclo

---

### Gerenciamento de threads
 
`iniciar_clientes()` cria todas as threads de clientes, inicia-as de forma concorrente e aguarda o término de todas.
 
**Funcionamento:**
1. Instancia `NUMERO_DE_CLIENTES` objetos `threading.Thread`, cada um apontando para `_rotina` com seu índice como argumento
2. Chama `.start()` em todas antes de chamar `.join()` em qualquer uma — garantindo que todas rodem simultaneamente
3. Aguarda o encerramento de todas com `.join()` antes de retornar

---

## 🐍 Programa principal

`main.py` é o ponto de entrada do programa. Responsável por unir as partes e inicializar a execução.

---
 
### Inicialização do sistema
 
_inicializar() é responsável por dar início as estruturas de dados globais do banqueiro.
 
**Passos:**
1. Define aleatoriamente a quantidade total de cada recurso em `disponivel` (entre `1` e `10`).
2. Gera valores aleatórios para `maximo` (entre `1` e o total de cada recurso).
3. Inicializa `alocacao` com zeros e `necessidade` igual a `maximo`.
4. Imprime o estado inicial do sistema.

---

### Execução da simulação

O trecho `if __name__ == "__main__":` chama `_inicializar()` para configurar o ambiente e depois `iniciar_clientes()` para começar a simulação.

---

## Considerações finais

```
Queridíssimo
     _                     ___                                 
    | |  _  _ __ __ _ ___ | _ )_ _ __ _ __ _ __ _ _ _  __ __ _ 
    | |_| || / _/ _` (_-< | _ \ '_/ _` / _` / _` | ' \/ _/ _` |
    |____\_,_\__\__,_/__/ |___/_| \__,_\__, \__,_|_||_\__\__,_|
                                        |___/           )_)     , vulgo Senhor das Estrelas ✨

Apesar da ajuda pontual do Claude ( IA da Antrophic que eu recomendo muito ), o código foi feito minuciosamente por mim numa quarta-feira à noite ouvindo trilha sonora de Baby Driver. Coisa boa...

Além disso fiz questão de dar uns toques especiais para melhorar a legibilidade e estética do programa, aproveite!!

Ass. Lucas Spiazzi
```