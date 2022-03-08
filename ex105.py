# Faça um programa que tenha um função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas;
# - A maior nota;
# - A menor nota;
# - A média da turma;
# - A situação(opcional);
# Adicione também as docstrings da função.


def notas(show=False):
    """
    :param show: mostra a situação da turma de acordo com o escolhido: True ou False
    :return: sem retorno
    """
    somanotas = 0
    d = dict()
    lista = list()
    qtdvalores = 0
    while True:
        n1 = float(input(f'Nota do aluno {qtdvalores}: '))
        somanotas += n1
        lista.append(n1)
        qtdvalores += 1
        d['Qtd notas'] = qtdvalores
        resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
        while resp != 'S' and resp != 'N':
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp == 'N':
            break
    d['Maior nota'] = max(lista)
    d['Menor nota'] = min(lista)
    d['Média da turma'] = somanotas / qtdvalores
    if show:
        if d['Média da turma'] < 5:
            d['Situação'] = 'Ruim'
        elif 5 <= d['Média da turma'] < 7:
            d['Situação'] = 'Razoável'
        else:
            d['Situação'] = 'Boa'
        print(d)
    else:
        print(d)


notas()
notas(show=True)
