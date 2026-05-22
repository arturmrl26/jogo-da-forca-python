# 🪢 Jogo da Forca — Python

Projeto desenvolvido como atividade avaliativa da disciplina de Lógica de Programação. Implementa o clássico Jogo da Forca em duas versões: uma para terminal e outra com interface gráfica, ambas escritas em Python.

---

## 📁 Estrutura do Repositório

```
jogo-da-forca/
│
├── jogo_forca_terminal.py            # Versão para terminal (desenvolvida manualmente)
├── jogo_forca_interface_grafica.py   # Versão com interface gráfica Tkinter (desenvolvida com auxílio de IA)
└── README.md
```

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- A biblioteca `tkinter` já vem incluída na instalação padrão do Python

### Versão Terminal

```bash
python jogo_forca_terminal.py
```

### Versão Gráfica

```bash
python jogo_forca_interface_grafica.py
```

---

## 🎮 Como Jogar

1. O programa sorteia uma palavra aleatória do banco de palavras
2. O jogador tenta adivinhar a palavra letra por letra
3. Cada letra errada revela uma parte do boneco na forca
4. O jogo termina com **vitória** (palavra completa) ou **derrota** (6 erros)
5. Ao fim de cada partida, é possível jogar novamente sem encerrar o programa

---

## ➕ Como Adicionar Palavras

As palavras estão definidas em uma lista dentro de cada arquivo. Para adicionar novas palavras, localize a variável `words` e insira os termos desejados:

**Em `jogo_forca_terminal.py` (linha 4) e `jogo_forca_interface_grafica.py` (linha 22):**

```python
words = [
    'programacao', 'dados', 'python', 'codigo', 'computador',
    'engenheiro', 'ciencia', 'maquina', 'jogador',
    'celular', 'imagem', 'internet', 'teclado', 'monitor', 'variavel',
    'sua_palavra_aqui',   # ← adicione aqui
    'outra_palavra',      # ← e aqui
]
```

> **Atenção:** use apenas letras minúsculas e sem acentos. O jogo não distingue maiúsculas de minúsculas durante a verificação.

---

## ✨ Ponto Extra — Inovação

A versão gráfica (`forcagrafica.py`) utiliza a biblioteca **Tkinter**, não abordada em sala de aula, para construir uma interface gráfica completa com:

- Canvas para desenho dinâmico do boneco
- Teclado virtual com feedback visual por cor (verde = acerto, vermelho = erro)
- Placar de pontos acumulado entre partidas
- Diálogos de fim de jogo com opção de reiniciar

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **random** — sorteio de palavras (biblioteca padrão)
- **tkinter** — interface gráfica (biblioteca padrão, ponto extra)

---

## 👨‍💻 Autoria

- Versão terminal (`JOGO_FORCA_TERMINAL.py`) — desenvolvida manualmente pelo autor
- Versão gráfica (`JOGO_FORCA_INTERFACE_GRAFICA.py`) — desenvolvida com auxílio de Inteligência Artificial
