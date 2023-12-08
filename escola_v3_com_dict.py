#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.2"

alunos = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "ingles": aula_ingles,
    "musica": aula_musica,
    "danca": aula_danca,
}

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades.items():

    print(f"Aluno da atividade: {nome_atividade}\n")
    print("-" * 40)

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(alunos["sala1"]) & set(atividade)
    atividade_sala2 = set(alunos["sala2"]).intersection(atividade)
               
    print("Sala1: ", atividade_sala1)
    print("Sala2: ", atividade_sala2)

    print()
    print("#" * 40)
