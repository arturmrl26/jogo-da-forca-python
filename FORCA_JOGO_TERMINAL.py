import random

# ─── LISTA DE PALAVRAS ────────────────────────────────────────────────────────
words = [
    'programacao', 'dados', 'python', 'codigo', 'computador',
    'engenheiro', 'ciencia', 'maquina', 'jogador',
    'celular', 'imagem', 'internet', 'teclado', 'monitor', 'variavel'
]

# ─── DESENHOS DO BONECO (6 estágios de erro) ──────────────────────────────────
boneco = [
    # 0 erros
    """
       -----
       |   |
       |
       |
       |
       |
    --------
    """,
    # 1 erro - cabeça
    """
       -----
       |   |
       |   O
       |
       |
       |
    --------
    """,
    # 2 erros - corpo
    """
       -----
       |   |
       |   O
       |   |
       |
       |
    --------
    """,
    # 3 erros - braço esquerdo
    """
       -----
       |   |
       |   O
       |  /|
       |
       |
    --------
    """,
    # 4 erros - braço direito
    """
       -----
       |   |
       |   O
       |  /|\\
       |
       |
    --------
    """,
    # 5 erros - perna esquerda
    """
       -----
       |   |
       |   O
       |  /|\\
       |  /
       |
    --------
    """,
    # 6 erros - perna direita (morreu)
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    --------
    """,
]

# ─── FUNÇÃO PRINCIPAL DO JOGO ─────────────────────────────────────────────────
def jogar():
    word = random.choice(words)
    letras_corretas = set()
    letras_erradas = set()
    max_erros = 6

    print("\n============================")
    print("    JOGO DA FORCA")
    print("============================")

    # ─── LOOP DA PARTIDA ──────────────────────────────────────────────────────
    while True:
        erros = len(letras_erradas)

        # Mostra o boneco no estágio atual
        print(boneco[erros])

        # Mostra letras erradas já tentadas
        print(f"  Erros ({erros}/{max_erros}): {' '.join(sorted(letras_erradas)) or '-'}")

        # Mostra a palavra com traços e letras descobertas
        palavra_exibida = ' '.join(
            letra if letra in letras_corretas else '_'
            for letra in word
        )
        print(f"\n  Palavra: {palavra_exibida}")
        print()

        # ─── VERIFICA VITÓRIA ─────────────────────────────────────────────────
        if all(letra in letras_corretas for letra in word):
            print("  ✓ PARABÉNS! VOCÊ GANHOU!")
            print(f"  A palavra era: {word.upper()}\n")
            return True

        # ─── VERIFICA DERROTA ─────────────────────────────────────────────────
        if erros >= max_erros:
            print(f"  ✗ VOCÊ PERDEU!")
            print(f"  A palavra era: {word.upper()}\n")
            return False

        # ─── LEITURA DA LETRA DO USUÁRIO ──────────────────────────────────────
        tentativa = input("  Digite uma letra: ").strip().lower()

        # Valida entrada
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("  ⚠ Digite apenas uma letra!\n")
            continue

        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("  ⚠ Você já tentou essa letra!\n")
            continue

        # ─── VERIFICA SE A LETRA ESTÁ NA PALAVRA ──────────────────────────────
        if tentativa in word:
            letras_corretas.add(tentativa)
            print("  ✓ Letra correta!\n")
        else:
            letras_erradas.add(tentativa)
            print("  ✗ Letra errada!\n")


# ─── LOOP DE SESSÃO: pergunta se quer jogar de novo ───────────────────────────
score = 0

while True:
    resultado = jogar()

    if resultado:
        score += 1

    print(f"  Pontuação: {score}")
    print("============================")

    jogar_de_novo = input("  Jogar novamente? (s/n): ").strip().lower()

    if jogar_de_novo != 's':
        print(f"\n  Obrigado por jogar! Pontuação final: {score}")
        print("============================\n")
        break