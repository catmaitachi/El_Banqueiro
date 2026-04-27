███████╗██╗      ██████╗  █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗██╗██████╗  ██████╗ 
 ██╔════╝██║      ██╔══██╗██╔══██╗████╗  ██║██╔═══██╗██║   ██║██╔════╝██║██╔══██╗██╔═══██╗
 █████╗  ██║      ██████╔╝███████║██╔██╗ ██║██║   ██║██║   ██║█████╗  ██║██████╔╝██║   ██║
 ██╔══╝  ██║      ██╔══██╗██╔══██║██║╚██╗██║██║▄▄ ██║██║   ██║██╔══╝  ██║██╔══██╗██║   ██║
 ███████╗███████╗ ██████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████╗██║██║  ██║╚██████╔╝
 ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝ 
                                                                                          

O objetivo deste projeto é implementar o **Algoritmo do Banqueiro**, um mecanismo de escalonamento e alocação de recursos voltado para a **prevenção de deadlocks** em sistemas operacionais. A aplicação simula um ambiente bancário onde múltiplos clientes (threads) solicitam e liberam instâncias de recursos limitados de forma concorrente.

A solução foca em três pilares fundamentais da computação paralela:
1.  **Gerenciamento de Threads:** Criação e controle de múltiplos fluxos de execução simultâneos.
2.  **Sincronização:** Uso de locks mutex para garantir a atomicidade das operações e evitar condições de corrida (*race conditions*).
3.  **Segurança de Estado:** Aplicação de lógica matemática para verificar se uma solicitação mantém o sistema em um "estado seguro", garantindo que a execução técnica seja livre de impasses.

## Alunos integrantes da equipe

<table align="center">
    <tr>
        <td align="center" width="50%"><a href="https://github.com/SEU-USER-AQUI"><img src="https://avatars.githubusercontent.com/u/SEU-ID-AQUI?v=4" alt="Perfil" style="width: 100%; height: auto; display: block;"></a></td>
        <td align="center" width="50%"><a href="https://github.com/USER-DUPLA-AQUI"><img src="https://avatars.githubusercontent.com/u/ID-DUPLA-AQUI?v=4" alt="Perfil" style="width: 100%; height: auto; display: block;"></a></td>
            <td align="center" width="50%"><a href="https://github.com/USER-DUPLA-AQUI"><img src="https://avatars.githubusercontent.com/u/ID-DUPLA-AQUI?v=4" alt="Perfil" style="width: 100%; height: auto; display: block;"></a></td>
    </tr>
    <tr>
        <td align="center">Nome do Aluno 1</td>
        <td align="center">Nome do Aluno 2</td>
        <td align="center">Isaías Alves de Souza Santos</td>
    </tr>
</table>

## Professore responsável

* [Lucas Bragança da Silva]


## 🛠️ Pré-requisitos: Instalação do Python

Este projeto requer o **Python 3.x**. Se você ainda não o tem instalado, siga as instruções presentes no link abaixo:

1. Siga o tutorial presente no link conforme o seu Sistema Operacional.
   
### Windows
https://python.org.br/instalacao-windows/

### Linux
https://python.org.br/instalacao-linux/

### MacOS X
https://python.org.br/instalacao-mac/

2. **Importante em caso de Windows:** No instalador, marque a opção **"Add Python to PATH"** antes de clicar em instalar.
4. Reinicie seu terminal e verifique a instalação com: `python --version`.
5. Caso o terminal retorne uma mensagem contendo a versão do Python, você instalou com suesso, siga para as instruções de execução.

## 🚀 Como Executar

Por se tratar de uma linguagem interpretada, o **Python não exige uma etapa de compilação manual** (como ocorre em C++ ou Java). O código-fonte é traduzido para *bytecode* e executado diretamente pelo interpretador.

**Passos:**
1. Abra o terminal de sua preferência.
2. Navegue até a pasta `code/` do projeto.
3. Execute o programa principal com o comando abaixo:

```bash
python main.py
```
*(Observação: dependendo do seu sistema operacional, pode ser necessário usar `python3 main.py`)*
