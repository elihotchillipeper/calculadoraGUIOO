# Documentação da Calculadora GUI OO

## Descrição
Esta é uma calculadora básica implementada em Python usando a biblioteca Tkinter para a interface gráfica. Ela suporta operações simples, como adição, subtração, multiplicação e divisão.

## Funcionalidades
- Realiza operações matemáticas básicas: adição, subtração, multiplicação e divisão.
- Exibe o resultado das operações na mesma tela.
- Permite a entrada de números e operadores matemáticos através de uma interface gráfica.

## Requisitos
- Python 3.x
- Biblioteca Tkinter (inclusa na instalação padrão do Python)

## Instalação

### Passo 1: Instalar Python
Certifique-se de que o Python 3.x está instalado em seu sistema. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

### Passo 2: Verificar Tkinter
Tkinter é uma biblioteca padrão do Python e deve estar incluída na sua instalação do Python. Para verificar se Tkinter está instalado, você pode executar o seguinte comando no terminal ou prompt de comando:
```bash
python -m tkinter
```
Se uma janela Tkinter aparecer, a biblioteca está instalada corretamente.

### Passo 3: Obter o Código
Clone o repositório ou baixe o arquivo contendo o código da calculadora.

Se estiver usando Git, execute:
```bash
git clone https://github.com/seuusuario/seurepositorio.git
```
Substitua o link pelo repositório onde o código está armazenado.

## Como Usar

### Executar o Programa

1. Vá até o diretório onde o arquivo Python (`calculadora.py`, por exemplo) está localizado.

2. Execute o programa com o seguinte comando:
   ```bash
   python calculadora.py
   ```
   Isso abrirá uma janela com a interface gráfica da calculadora.

### Interface e Funcionalidade

- **Tela de Entrada**: Exibe os números e operações atuais. Use o teclado ou clique nos botões para inserir valores e operadores.
  
- **Botões**:
  - **Números (0-9)**: Insere o número correspondente na tela.
  - **Operadores (+, -, *, /)**: Adiciona o operador selecionado à expressão.
  - **.**: Adiciona um ponto decimal.
  - **C**: Limpa a tela.
  - **=**: Avalia a expressão matemática e exibe o resultado.

### Exemplo de Uso
1. Clique nos botões para inserir uma expressão matemática, por exemplo: `5`, `+`, `3`, `*`, `2`.
2. Clique no botão `=` para calcular o resultado, que será exibido na tela.
3. Se desejar limpar a tela, clique no botão `C`.

## Personalização
- **Personalização**: A interface e funcionalidades podem ser ampliadas para incluir mais recursos, como suporte a operações avançadas ou histórico de cálculos.
