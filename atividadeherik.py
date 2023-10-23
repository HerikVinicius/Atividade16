situacao = str(input(f"vc é idoso, gestante, cadeirante ou nenhum desses?\nDigite 'idoso', 'gestante', 'cadeirante' ou 'nenhum': "))

if situacao == 'idoso' or situacao == 'gestante' or situacao == 'cadeirante':
    print("vc tem acesso a fila de prioridade.")
else:
    print("vc não tem acesso a fila de prioridade.")