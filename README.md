```

 ███████╗██╗      ██████╗  █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗██╗██████╗  ██████╗ 
 ██╔════╝██║      ██╔══██╗██╔══██╗████╗  ██║██╔═══██╗██║   ██║██╔════╝██║██╔══██╗██╔═══██╗
 █████╗  ██║      ██████╔╝███████║██╔██╗ ██║██║   ██║██║   ██║█████╗  ██║██████╔╝██║   ██║
 ██╔══╝  ██║      ██╔══██╗██╔══██║██║╚██╗██║██║▄▄ ██║██║   ██║██╔══╝  ██║██╔══██╗██║   ██║
 ███████╗███████╗ ██████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████╗██║██║  ██║╚██████╔╝
 ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝ 

```                                                                                       

O objetivo deste projeto é implementar o **Algoritmo do Banqueiro**, um mecanismo de escalonamento e alocação de recursos voltado para a **prevenção de deadlocks** em sistemas operacionais. A aplicação simula um ambiente bancário onde múltiplos clientes (threads) solicitam e liberam instâncias de recursos limitados de forma concorrente.

A solução foca em três pilares fundamentais da computação paralela:

| Pilar | Descrição |
|------|-----------|
| **Gerenciamento de Threads** | Criação e controle de múltiplos fluxos de execução simultâneos. |
| **Sincronização** | Uso de *locks mutex* para garantir a atomicidade das operações e evitar *condições de corrida*. |
| **Segurança de Estado** | Aplicação de lógica matemática para verificar se uma solicitação mantém o sistema em um "estado seguro", garantindo que a execução técnica seja livre de impasses. |

> Mais detalhes do funcionamento do algoritmo estão disponíveis na [documentação do código](./code/README.md).

## Alunos integrantes da equipe

<table align="center">
    <tr>
        <td align="center" width="33%"><a href="https://github.com/Santos5-bh"><img src="https://avatars.githubusercontent.com/u/199308214?s=400&u=2266a89af9d798c5d00430c1ac8ec03d7d143464&v=4" alt="Perfil" style="width: 100%; height: auto; display: block;"></a></td>
        <td align="center" width="33%"><a href="https://github.com/isaias-alves"><img src="https://avatars.githubusercontent.com/u/199569676?v=4" alt="Perfil" style="width: 100%; height: auto; display: block;"></a></td>
        <td align="center" width="33%"><a href="https://github.com/catmaitachi"><img src="https://avatars.githubusercontent.com/u/108273480?v=4" alt="Perfil" style="width: 100%; height: auto; display: block;"></a></td>
    </tr>
    <tr>
        <td align="center">Gabriel Santos Martins</td>
        <td align="center">Isaías Alves de Souza Santos</td>
        <td align="center">Lucas Moraes Rocha Spiazzi</td>
    </tr>
</table>

## Professor responsável

* Lucas Bragança da Silva

## 🚀 Como Executar

**Pré-requisitos:** Certifique-se de ter o **Python 3.x** instalado em sua máquina com o comando `python --version` ou `python3 --version`. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/downloads/).

**Passos:**

1. Clone este repositório para sua máquina local usando o comando:
   
   ```bash
   git clone https://github.com/catmaitachi/El_Banqueiro.git
   ```

2. Navegue até o diretório do projeto:
   
   ```bash
   cd El_Banqueiro/code
   ```

3. Execute o script principal para iniciar a simulação do Algoritmo do Banqueiro:
   
   ```bash
    python main.py || python3 main.py
    ```
