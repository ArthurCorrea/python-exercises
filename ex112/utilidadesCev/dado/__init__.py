def leiaDinheiro(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'\033[1;31mERRO! \"{entrada}\" é um valor inválido!\033[m')
        else:
            ok = True
            return float(entrada)
