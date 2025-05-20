def meta( tipo_treino):
    
        if sum(vetor) <= 0:
            while True:
                try:   
                    tipo_treino = input(str("Digite o tipo de treino: "))
                    break
                except ValueError:
                    print('Entrada inválida. Digite seu treino: ')


        while True:
            try:
                metas = int(input("Digite a sua meta para a semana (número): "))
                break
            except ValueError:
                print('Entrada inválida. Digite um número.')
        while True:
            try:
                progresso = int(input("Digite o progresso do dia: "))
                vetor.append(progresso)
                break
            except ValueError:
                print('Entrada inválida. Digite um número.')
              
        print("digite 000 em (progresso do dia) para apagar suas metas")
        if progresso == 000 :
            metas = 0
            tipo_treino = " "
            vetor.clear()
        print(f"Progresso {tipo_treino}: {sum(vetor)} de {metas}")
    
        return vetor, metas, tipo_treino