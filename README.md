# Conversão de AFN para AFD

<div align="center">
  <img src="https://img.shields.io/badge/Versão-1.0-blue.svg" alt="Versão 1.0">
  <img src="https://img.shields.io/badge/Licença-MIT-green.svg" alt="Licença MIT">
</div>

---

## Resumo do Trabalho

> Este projeto tem como objetivo implementar a conversão de um Autômato Finito Não-determinístico (AFN) para um Autômato Finito Determinístico (AFD), utilizando Python. A conversão é essencial para eliminar a não-determinização, garantindo que o autômato resultante seja determinístico, mais eficiente e utilizável em aplicações práticas, como análise de padrões e compiladores. O projeto inclui visualização gráfica para ilustrar os estados e transições dos autômatos.

---

## Descrição

> O projeto utiliza um conjunto de funções em Python para realizar a conversão de AFN para AFD. As principais etapas incluem:
>
> - Representação do AFN em estrutura de dados (`dicionários` e `conjuntos`).
> - Manipulação de transições e estados, incluindo o cálculo do **fecho vazio**.
> - Conversão para um AFD, criando novos estados combinados e eliminando transições vazias.
> - Geração de gráficos usando a biblioteca Graphviz para facilitar a compreensão dos autômatos.
>
> ### Funcionalidades
> - Conversão automática de AFN para AFD.
> - Modo interativo para o usuário criar e visualizar autômatos personalizados.
> - Gráficos detalhados mostrando as transições e os estados finais de cada autômato.
>
> ### Tecnologias Utilizadas
> - **Python 3.8+**
> - **Graphviz** para visualização gráfica.
>
> ### Metodologia
> - Cada função no código foi projetada para refletir os conceitos teóricos de autômatos, garantindo que os princípios matemáticos sejam traduzidos para o código.

---

## Como Executar

### Requisitos:
- **Python 3.8+**
- **Graphviz** (para visualização gráfica)
- Biblioteca Python para manipulação do Graphviz.

### Instalando as Dependências:
1. Certifique-se de que o **Python** está instalado no sistema.
   - Verifique a versão com:
     ```bash
     python --version
     ```
2. Instale o **Graphviz** no sistema:
   - **Ubuntu/Linux**:
     ```bash
     sudo apt update
     sudo apt install graphviz
     ```
   - **Windows**:
     - Baixe o instalador no [site oficial do Graphviz](https://graphviz.org/download/).
     - Durante a instalação, marque a opção para adicionar o Graphviz ao **PATH** do sistema.
   - **macOS**:
     ```bash
     brew install graphviz
     ```

3. Instale a biblioteca Python para manipular o Graphviz:
   ```bash
   pip install graphviz
   ```

4. Verifique se o Graphviz foi instalado corretamente:
   ```bash
   dot -version
   ```

---

### Modo Base (Exemplo Pré-definido):
1. Salve o arquivo principal como `main.py`.
2. No terminal, execute o seguinte comando:
   ```bash
   python main.py --base
   ```
3. O programa executará um exemplo pré-definido:
   - Criará um **Autômato Finito Não Determinístico (AFN)** e o converterá para um **Autômato Finito Determinístico (AFD)**.
   - Exibirá os detalhes de cada autômato no console.
   - Gerará gráficos salvos como `afn.png` e `afd.png` no diretório do projeto.

---

### Modo Interativo (Criação Personalizada):
1. Execute o arquivo principal sem argumentos:
   ```bash
   python main.py
   ```
2. Insira os dados solicitados no terminal:
   - **Estados do autômato** (ex.: `0,1,2`).
   - **Estado inicial** (ex.: `0`).
   - **Estados finais** (ex.: `2`).
   - **Transições** no formato `origem,letra,destino` (ex.: `0,a,1`). Digite **"fim"** para encerrar a entrada de transições.
3. Após inserir os dados:
   - O programa exibirá o AFN e o AFD no console.
   - Os gráficos correspondentes serão gerados como `afn_interativo.png` e `afd_interativo.png`.

---

### Dicas Importantes:
1. **Problemas com o Graphviz?**
   - Se os gráficos não forem gerados, certifique-se de que o **Graphviz** está corretamente configurado no **PATH**.
   - No Windows, adicione manualmente o caminho do executável `dot.exe` nas variáveis de ambiente.
   
2. **Execução em Ambientes Virtuais**:
   - Recomenda-se usar um ambiente virtual para isolar as dependências:
     ```bash
     python -m venv venv
     source venv/bin/activate  # No Linux/macOS
     venv\Scripts\activate     # No Windows
     pip install graphviz
     ```

3. **Logs e Depuração**:
   - Verifique o console para mensagens de erro ou logs adicionais.

---

## Estrutura do Repositório 

- **`/apresentacoes/`**: Slides e vídeos explicativos sobre o projeto.
- **`/docs/`**: Documentação técnica, incluindo diagramas e exemplos de uso.
- **`main.py`**: Executa a configuração base e o modo interativo.
- **`automata.py`**: Contém as funções auxiliares, como cálculo de fecho vazio e geração de gráficos.
- **`/assets/`**: Imagens geradas pelos gráficos e outros recursos estáticos.

---

## Autores

- [William Valther Silva Martins](mailto:william.valther@discente.ufma.br)  
- [Victor Ferreira Braga](mailto:victor.braga@discente.ufma.br)  

---

## Agradecimentos

- **Universidade Federal do Maranhão (UFMA)**  
- **Professor Doutor Thales Levi Azevedo Valente**  
- **Colegas de curso**

Agradecemos a todas as pessoas e instituições que contribuíram para a realização deste projeto.

## Copyright / License

Este projeto foi desenvolvido como parte da disciplina **LINGUAGENS FORMAIS E AUTÔMATOS**, sob a orientação do professor **Dr. Thales Levi Azevedo Valente**, durante o semestre letivo **2024.2**, do curso de **Engenharia da Computação** na Universidade Federal do Maranhão (**UFMA**).

O material é licenciado sob a **Licença MIT**: você pode usá-lo livremente para fins acadêmicos e comerciais, desde que dê os devidos créditos. Para mais detalhes, consulte a seção de licença abaixo.

---

<div align="center">
Feito com ♥ por <strong>Alunos UFMA</strong>
</div>
