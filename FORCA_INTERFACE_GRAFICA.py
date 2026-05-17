import random
from tkinter import *
from tkinter import messagebox

# ─── ESTADO GLOBAL DA SESSÃO ───────────────────────────────────────────────────
run = True
score = 0

# ─── LOOP PRINCIPAL: cada iteração = uma partida ──────────────────────────────
while run:

    root = Tk()
    root.geometry('905x700')
    root.title('JOGO DA FORCA')
    root.config(bg='#ffffe7')

    # Variáveis de controle da partida
    count = 0
    win_count = 0

    # ─── SORTEIO DA PALAVRA ───────────────────────────────────────────────────
    words = [
        'programacao', 'dados', 'python', 'codigo', 'computador',
        'engenheiro', 'ciencia', 'maquina', 'jogador',
        'celular', 'imagem', 'internet', 'teclado', 'monitor', 'variavel'
    ]
    word = random.choice(words)

    # ─── CANVAS: desenha a forca e o boneco ───────────────────────────────────
    canvas = Canvas(root, width=400, height=380, bg='#ffffe7', highlightthickness=0)
    canvas.place(x=50, y=60)

    # Estrutura da forca (estática, desenhada uma vez)
    canvas.create_line(20, 360, 200, 360, width=5, fill='#5a3e1b')  # base
    canvas.create_line(100, 360, 100, 20,  width=5, fill='#5a3e1b')  # poste vertical
    canvas.create_line(100, 20,  260, 20,  width=5, fill='#5a3e1b')  # topo horizontal
    canvas.create_line(260, 20,  260, 60,  width=5, fill='#5a3e1b')  # corda

    # Partes do boneco — cada parte é um objeto do canvas, oculto inicialmente
    # Criamos todos e guardamos os IDs para revelar um a um conforme os erros
    cabeca  = canvas.create_oval(235, 60, 285, 110, width=3, outline='#222', state=HIDDEN)
    corpo   = canvas.create_line(260, 110, 260, 210, width=3, fill='#222', state=HIDDEN)
    braco_e = canvas.create_line(260, 130, 210, 170, width=3, fill='#222', state=HIDDEN)
    braco_d = canvas.create_line(260, 130, 310, 170, width=3, fill='#222', state=HIDDEN)
    perna_e = canvas.create_line(260, 210, 210, 270, width=3, fill='#222', state=HIDDEN)
    perna_d = canvas.create_line(260, 210, 310, 270, width=3, fill='#222', state=HIDDEN)

    # Lista ordenada: cada erro revela a próxima parte
    partes_boneco = [cabeca, corpo, braco_e, braco_d, perna_e, perna_d]

    # ─── TRAÇOS DA PALAVRA ────────────────────────────────────────────────────
    # Centraliza os traços horizontalmente na tela
    dashes = []
    total_width = len(word) * 50
    start_x = (905 - total_width) // 2

    for i in range(len(word)):
        x_pos = start_x + i * 50
        lbl = Label(root, text='_', bg='#ffffe7', font=('Arial', 36, 'bold'), fg='#333')
        lbl.place(x=x_pos, y=430)
        dashes.append(lbl)

    # ─── PLACAR ───────────────────────────────────────────────────────────────
    score_label = Label(root, text=f'PONTOS: {score}', bg='#ffffe7',
                        font=('Arial', 22, 'bold'), fg='#333')
    score_label.place(x=10, y=10)

    # Contador de erros visível
    erros_label = Label(root, text='ERROS: 0/6', bg='#ffffe7',
                        font=('Arial', 14), fg='#c0392b')
    erros_label.place(x=10, y=50)

    # ─── FUNÇÃO: VERIFICAR LETRA CLICADA ─────────────────────────────────────
    def verificar_letra(letra, botao):
        global count, win_count, run, score

        # Desativa o botão visualmente ao invés de destruir,
        # assim não perde a referência ao objeto
        botao.config(state=DISABLED, relief=SUNKEN, fg='#aaaaaa', bg='#e0e0e0')

        if letra in word:
            # ── Letra correta: revela na palavra ─────────────────────────────
            botao.config(bg='#2ecc71', fg='white')   # verde = acerto
            for i in range(len(word)):
                if word[i] == letra:
                    win_count += 1
                    dashes[i].config(text=letra.upper(), fg='#27ae60')

            # Verifica vitória
            if win_count == len(word):
                score += 1
                score_label.config(text=f'PONTOS: {score}')
                resposta = messagebox.askyesno(
                    'FIM DE JOGO',
                    f'🎉 VOCÊ GANHOU!\nPontuação: {score}\n\nJogar novamente?'
                )
                run = resposta
                root.destroy()
        else:
            # ── Letra errada: revela parte do boneco ─────────────────────────
            botao.config(bg='#e74c3c', fg='white')   # vermelho = erro
            count += 1
            erros_label.config(text=f'ERROS: {count}/6')

            # Revela a próxima parte do boneco no canvas
            canvas.itemconfig(partes_boneco[count - 1], state=NORMAL)

            # Verifica derrota
            if count == 6:
                resposta = messagebox.askyesno(
                    'FIM DE JOGO',
                    f'💀 VOCÊ PERDEU!\nA palavra era: {word.upper()}\n\nJogar novamente?'
                )
                if resposta:
                    run = True
                    score = 0
                else:
                    run = False
                root.destroy()

    # ─── BOTÕES DAS LETRAS A-Z ────────────────────────────────────────────────
    # Cores alternadas para deixar o teclado colorido e divertido
    cores = ['#3498db','#9b59b6','#e67e22','#27ae60','#e74c3c','#1abc9c',
             '#f39c12','#2980b9','#8e44ad','#16a085','#d35400','#c0392b',
             '#2ecc71','#e91e63','#00bcd4','#ff5722','#607d8b','#795548',
             '#ff9800','#4caf50','#03a9f4','#9c27b0','#ff5252','#00e676',
             '#ffeb3b','#f44336']

    letras = 'abcdefghijklmnopqrstuvwxyz'

    # Primeira linha: A até M (13 letras)
    for idx, letra in enumerate(letras[:13]):
        def fazer_comando(l, b_ref):
            return lambda: verificar_letra(l, b_ref)

        btn = Button(
            root, text=letra.upper(), bd=0,
            font=('Arial', 13, 'bold'),
            fg='white', bg=cores[idx],
            activebackground=cores[idx],
            width=4, height=2,
            cursor='hand2',
            relief=RAISED
        )
        btn.config(command=fazer_comando(letra, btn))
        btn.place(x=idx * 68, y=570)

    # Segunda linha: N até Z (13 letras)
    for idx, letra in enumerate(letras[13:]):
        def fazer_comando(l, b_ref):
            return lambda: verificar_letra(l, b_ref)

        btn = Button(
            root, text=letra.upper(), bd=0,
            font=('Arial', 13, 'bold'),
            fg='white', bg=cores[13 + idx],
            activebackground=cores[13 + idx],
            width=4, height=2,
            cursor='hand2',
            relief=RAISED
        )
        btn.config(command=fazer_comando(letra, btn))
        btn.place(x=idx * 68, y=630)

    # ─── BOTÃO SAIR ───────────────────────────────────────────────────────────
    def sair():
        global run
        resposta = messagebox.askyesno('SAIR', 'Deseja sair do jogo?')
        if resposta:
            run = False
            root.destroy()

    btn_sair = Button(root, text='SAIR', command=sair,
                      bg='#e74c3c', fg='white', font=('Arial', 13, 'bold'),
                      bd=0, padx=12, pady=6, cursor='hand2')
    btn_sair.place(x=810, y=15)

    # ─── INICIA O LOOP DE EVENTOS ─────────────────────────────────────────────
    root.mainloop()