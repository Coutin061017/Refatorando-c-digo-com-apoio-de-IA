def ler_quantidade_notas():
    """Pergunta quantas notas serão digitadas, validando a entrada."""
    while True:
        try:
            n = int(input("Quantas notas? "))
            if n <= 0:
                print("Digite um número inteiro maior que zero.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_notas(quantidade):
    """Lê 'quantidade' notas do usuário, validando cada uma (entre 0 e 10)."""
    notas = []
    for i in range(quantidade):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1}: "))
                if not 0 <= nota <= 10:
                    print("A nota deve estar entre 0 e 10.")
                    continue
                notas.append(nota)
                break
            except ValueError:
                print("Entrada inválida. Digite um número (ex: 7.5).")
    return notas


def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)


def verificar_aprovacao(media, media_minima=6):
    """Retorna True se a média for suficiente para aprovação."""
    return media >= media_minima


def main():
    n = ler_quantidade_notas()
    notas = ler_notas(n)
    media = calcular_media(notas)
    situacao = "aprovado" if verificar_aprovacao(media) else "reprovado"

    print(f"\nNotas digitadas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


if __name__ == "__main__":
    main()
