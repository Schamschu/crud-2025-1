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