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
    