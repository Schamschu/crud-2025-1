import os
os.system('cls')
import random

vetor = [] 

def menu ():
    metas = 0
    tipo_treino = " "
    lista_de_semana = []
    while True: 
        print('\n----- Menu -----')
        print('1. Adicionar')
        print('2. Visualizar')
        print('3. Editar')
        print('4. Excluir')
        print('5. Filtrar')
        print('6. Metas e Desempenho')
        print('7. Sugestão de Treino')
        print('8. Funcionalidade extra')
        print('9. Sair')

        try:
            escolha = int(input('\nInforme a opção desejada: '))
            if escolha == 9:
                break

            elif escolha == 1:
                vetor= adicionar(metas,tipo_treino)# ta tudo certo so preciso resolver essa parte!!! to chmando a função não a variavel /resolvi esse caralho

            elif escolha == 2:
                visualizar()

            elif escolha == 3:
                editar()

            elif escolha == 4:
                excluir()

            elif escolha == 5:
                filtrar()

            elif escolha == 6:
                vetor, metas, tipo_treino = meta(tipo_treino)

            elif escolha == 7:
                lista_de_semana = randomico(lista_de_semana )
            
            elif escolha == 8:
                calcular_tmb()
            
            else:
                print('\nNúmero inválido, tente novamente!')
                continue
       
        except ValueError:
            print("\nPor favor, insira um número!")
            continue

def adicionar(metas,tipo_treino):
    with open('treinos.txt', 'r') as file:
        linhas = file.readlines()

    cont = len(linhas) + 1 

    with open('treinos.txt', 'a') as file: 
        print('\n----- Adicionar -----')
        data = input('Informe a data: ')
        tipo = input('Informe o tipo de treino (AMRAP, EMOM, For Time): ')
        tempo = input('Informe a duração do treino em min:  ')
        movimentos = input('Informe os movimentos: ')

        treino = (f'{cont}. Data: {data} | Tipo: {tipo} | Minutos: {tempo} min | Movimentos: {movimentos}\n')
        file.write(treino)
        
        print('\nTreino adicionado com sucesso!')
    if sum(vetor)>0:
        while True:
            try:
                progresso = int(input("Digite o progresso do dia: "))
                vetor.append(progresso)
                break
            except ValueError:
                print('Entrada inválida. Digite um número.')
            
            
        print("progresso ",tipo_treino," ",sum(vetor), " de ", metas)
        if sum(vetor)>0 and sum(vetor) == metas:
            print("Meta atingida :)")
        elif sum(vetor) > metas:
            print("VOCÊ SUPEROU SUA META!!")
        return vetor


def visualizar():
    print('\n----- Visualizar -----')
    try:
        with open ('treinos.txt', 'r') as file:
            for linha in file:
                print(linha.strip())
    except FileNotFoundError:
        print('Nenhum treino cadastrado!')

def editar():
    try:
        with open ('treinos.txt','r') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        print('Nenhum treino cadastrado!')
        return
    
    print('\n----- Editar Treino -----')

    for linha in linhas:
        print(linha.strip())

    try:
        escolha = int(input('\nInforme o número do treino que deseja alterar: '))
        if escolha < 1 or escolha > len(linhas):
            print('Treinos não existentes!')
            return
    except ValueError:
        print('Entrada inválida. Digite um número!')
        return

    indice = escolha - 1
    partes = linhas[indice].strip().split('|')

    data_nova = input(f'Nova data ({partes[0].split(":")[1].strip()}): ')
    tipo_novo = input(f'Novo tipo ({partes[1].split(":")[1].strip()}): ')
    tempo_novo = input(f'Novo tempo ({partes[2].split(":")[1].strip()}): ')
    movimentos_novo = input(f'Novo movimento ({partes[3].split(":")[1].strip()}): ')

    linhas[indice] = (f"{escolha}. Data: {data_nova} | Tipo: {tipo_novo} | Tempo: {tempo_novo} | Movimentos: {movimentos_novo}\n")

    with open('treinos.txt', 'w') as file:
        file.writelines(linhas)

    print("\nTreino atualizado com sucesso!")

def excluir():
    try:
        with open ('treinos.txt', 'r') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        print('Nenhum treino cadastrado!')
        return
        
    print('\n----- Excluir Treino -----')
        
    for linha in linhas:
        print(linha.strip())

    try:
        escolha = int(input('\nInforme o número do treino que deseja excluir: '))
        if escolha < 1 or escolha > len(linhas):
            print('Treinos não existentes.')
            return
    except ValueError:
        print('Entrada inválida. Digite um número.')
        return
        
    treino_removido = linhas.pop(escolha - 1)

    contador = 1
    for i in range(len(linhas)):
        partes = linhas[i].split('. ', 1)
        if len(partes) > 1:
            linhas[i] = f"{contador}. {partes[1]}"
            contador += 1

    with open('treinos.txt', 'w') as file:
        file.writelines(linhas)

    print(f"Treino: [{treino_removido}] removido com sucesso!")

def filtrar():
    try:
        with open('treinos.txt', 'r') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        print('Nenhum treino cadastrado!')
        return
    


    print('\n----- Filtrar Treinos -----')
    print('\n[1] Filtrar por Tipo de Treino')
    print('[2] Filtrar por Movimento')

    while True:
            try:
                opcao = int(input('Escolha a opção de filtro: '))
                if opcao in [1, 2]:
                    break
                else:
                    print('Opção inválida. Por favor, escolha 1 ou 2.')
            except ValueError:
                print('Entrada inválida. Digite um número.')

    resultados = []
    informacao = ""

    if opcao == 1:
        tipo_busca = input('Digite o tipo de treino para filtrar: ').lower()
        informacao = f"Treinos do tipo '{tipo_busca}'"
        for linha in linhas:
            if tipo_busca in linha.lower().split('|')[1]:
                resultados.append(linha.strip())

    elif opcao == 2:
        movimento_busca = input('Digite o movimento para filtrar: ').lower()
        informacao = f"Treinos com o movimento '{movimento_busca}'"
        for linha in linhas:
            if movimento_busca in linha.lower().split('|')[3]:
                resultados.append(linha.strip())
    else:
        print('Opção de filtro inválida.')
        return

    print(f'\n----- {informacao} -----')
    if resultados:
        for resultado in resultados:
            print(resultado)
    else:
        print('Nenhum treino encontrado com este critério.')

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

def randomico(lista_de_semana):
    lista_de_treino= [
         "Durante 30 minutos, a cada início de minuto, execute:\n5 Pull-ups (barra fixa)\n10 Push-ups (flexões)\n15 Air Squats (agachamentos livres)",
         "Para tempo (cronômetro):\n1 km de corrida\n100 Pull-ups\n200 Push-ups\n300 Air Squats\n1 km de corrida",
         "Para tempo:\n10 a 1 repetições de:\nKettlebell Swings (peso moderado)\nDumbbell Thrusters (peso moderado)",
         "Para tempo:\n400 m de corrida\n40 Air Squats\n30 Sit-ups\n20 Burpees\n10 Pull-ups\n400 m de corrida",
         "3 rounds para tempo:\n10 Air Squats\n10 Sit-ups\n10 Push-ups\n10 Ring Rows (ou remada invertida)\n10 Burpees",
         "3 rounds for time:\n500m de remo\n40 agachamentos livres\n30 abdominais\n20 flexões de braço\n10 pull-ups (barra fixa)",
         "Para tempo:\n800m de corrida\n40 agachamentos overhead (com barra leve)\n40 saltos sobre caixa (box jump overs)\n40 sumo deadlift high pulls (com barra leve)\n800m de corrida"
        ]
    if len(lista_de_treino) == len(lista_de_semana):
            print("voce fez todos os treinos da semana")
            return lista_de_semana
    while True:
        aleatorio = random.choice(lista_de_treino)
        
        if aleatorio not in lista_de_semana:
            lista_de_semana.append(aleatorio)
            
            
            print(aleatorio)
            break
    return lista_de_semana


def calcular_tmb():
    while True:
        sexo = input("Digite (F) para sexo feminino\nDigite (M) para sexo masculino\n---> ").strip().upper()
        if sexo in ['F', 'M']:
            break
        else:
            print("Entrada inválida. Por favor, digite 'F' para feminino ou 'M' para masculino.")

    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            if peso > 0:
                break
            else:
                print("O peso deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o peso.")

    while True:
        try:
            altura = float(input("Digite sua altura em cm: "))
            if altura > 0:
                break
            else:
                print("A altura deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para a altura.")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0:
                break
            else:
                print("A idade deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido para a idade.")

    if sexo == 'F':
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    else:  
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)

    print(f"Sua Taxa Metabólica Basal é: {tmb:.2f} Kcal")

    return
menu()