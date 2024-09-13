# Tabelas

zoo_table = dict()
animals_table = dict()

zoo_table = {"numero": ["1", "2", "3", "4", "5"], 
             "bioma": ["savana", "floresta", "savana e rio", "rio", "savana"], 
             "tamanho total": [10, 5, 7, 8, 9], 
             "tamanho restante": [7, 5, 5, 8, 6],
             "animais existentes": [["macaco"], [], ["gazela"], [], ["leao"]] }

animals_table = {"especie": ["leao", "leopardo", "crocodilo", "macaco", "gazela", "hipopotamo"],
                 "tamanho": [3, 2, 3, 1, 2, 4], 
                 "bioma": ["savana", "savana", "rio", "savana ou floresta", "savana", "savana ou rio"] }



def analisaRecintos(animal, quantidade):
    animal = animal.lower()
    
    tamanhoAnimal = None
    biomaAnimal = None
    animaisCarnivoros = ["leao", "leopardo", "crocodilo"]

    if animal == "macaco":
        tamanhoAnimal = animals_table["tamanho"][animals_table["especie"].index("macaco")]
        biomaAnimal = animals_table["bioma"][animals_table["especie"].index("macaco")].split(" ") #savana ou floresta
        for index, bioma in enumerate(zoo_table["bioma"]):
            
            
            bioma = bioma.split(" ") 
            
            # Calcula a diferença de animais no bioma, checa se tem tipo mamifero ou carnivoro, cria variável com a diferença de tamanho para diferentes espécies de cada animal
            animaisBioma = len(zoo_table["animais existentes"][index])
            contemCarnivoro = False

            if (animaisBioma > 0):
                
                for animalExistente in zoo_table["animais existentes"][index]:
                    if animalExistente in animaisCarnivoros:
                        contemCarnivoro = True
                    
                    if animalExistente == "macaco":
                        animaisBioma -= 1       
                      
            for e in bioma:
                # Macacos não ficam sozinhos no bioma
                if (animaisBioma == 0) and (quantidade < 2):
                    continue

                if (e in biomaAnimal) and (contemCarnivoro == False): 
                    if zoo_table["tamanho restante"][index] - animaisBioma >= tamanhoAnimal * quantidade:
                        print("Recinto {} (espaço livre: {} total: {}".format(index+1, zoo_table["tamanho restante"][index] - (tamanhoAnimal  * quantidade) - animaisBioma, zoo_table["tamanho total"][index]))
                    else:
                        print("Não há recinto viável")


    elif animal == "leao":
        tamanhoAnimal = animals_table["tamanho"][animals_table["especie"].index("leao")]
        biomaAnimal = animals_table["bioma"][animals_table["especie"].index("leao")].split(" ")
        for index, bioma in enumerate(zoo_table["bioma"]):

            bioma = bioma.split(" ")

            # Calcula a diferença de animais no bioma, checa se tem tipo mamifero ou carnivoro, cria variável com a diferença de tamanho para diferentes espécies de cada animal
            animaisBioma = len(zoo_table["animais existentes"][index])
            contemCarnivoro = False

            if (animaisBioma > 0):
                
                for animalExistente in zoo_table["animais existentes"][index]:
                    if animalExistente in animaisCarnivoros:
                        contemCarnivoro = True
                    
                    if animalExistente == "leao":
                        animaisBioma -= 1 

            for e in bioma:
                if (e in biomaAnimal and ((animaisBioma == 0) or (contemCarnivoro == True))):
                    if zoo_table["tamanho restante"][index] - animaisBioma >= tamanhoAnimal * quantidade:
                        print("Recinto {} (espaço livre: {} total: {}".format(index+1, zoo_table["tamanho restante"][index] - (tamanhoAnimal  * quantidade) - animaisBioma, zoo_table["tamanho total"][index]))
                    else:
                        print("Não há recinto viável")   

    elif animal == "leopardo":
        tamanhoAnimal = animals_table["tamanho"][animals_table["especie"].index("leopardo")]
        biomaAnimal = animals_table["bioma"][animals_table["especie"].index("leopardo")].split(" ")
        for index, bioma in enumerate(zoo_table["bioma"]):

            bioma = bioma.split(" ")

            # Calcula a diferença de animais no bioma, checa se tem tipo carnivoro, cria variável com a diferença de tamanho para diferentes espécies de cada animal
            animaisBioma = len(zoo_table["animais existentes"][index])
            contemCarnivoro = False

            if (animaisBioma > 0):
                
                for animalExistente in zoo_table["animais existentes"][index]:
                    if animalExistente in animaisCarnivoros:
                        contemCarnivoro = True
                    
                    if animalExistente == "leopardo":
                        animaisBioma -= 1 

            for e in bioma:
                if (e in biomaAnimal and ((animaisBioma == 0) or (contemCarnivoro == True))):
                    if zoo_table["tamanho restante"][index] - animaisBioma >= tamanhoAnimal * quantidade:
                        print("Recinto {} (espaço livre: {} total: {}".format(index+1, zoo_table["tamanho restante"][index] - (tamanhoAnimal  * quantidade) - animaisBioma, zoo_table["tamanho total"][index]))
                    else:
                        print("Não há recinto viável") 


    elif animal == "crocodilo":
        tamanhoAnimal = animals_table["tamanho"][animals_table["especie"].index("crocodilo")]
        biomaAnimal = animals_table["bioma"][animals_table["especie"].index("crocodilo")].split(" ")
        for index, bioma in enumerate(zoo_table["bioma"]):

            bioma = bioma.split(" ")

            # Calcula a diferença de animais no bioma, checa se tem tipo carnivoro, cria variável com a diferença de tamanho para diferentes espécies de cada animal
            animaisBioma = len(zoo_table["animais existentes"][index])
            contemCarnivoro = False

            if (animaisBioma > 0):
                
                for animalExistente in zoo_table["animais existentes"][index]:
                    if animalExistente in animaisCarnivoros:
                        contemCarnivoro = True
                    
                    if animalExistente == "crocodilo":
                        animaisBioma -= 1 

            for e in bioma:
                if (e in biomaAnimal and ((animaisBioma == 0) or (contemCarnivoro == True))):
                    if zoo_table["tamanho restante"][index] - animaisBioma >= tamanhoAnimal * quantidade:
                        print("Recinto {} (espaço livre: {} total: {}".format(index+1, zoo_table["tamanho restante"][index] - (tamanhoAnimal  * quantidade) - animaisBioma, zoo_table["tamanho total"][index]))
                    else:
                        print("Não há recinto viável")

    elif animal == "gazela":
        tamanhoAnimal = animals_table["tamanho"][animals_table["especie"].index("gazela")]
        biomaAnimal = animals_table["bioma"][animals_table["especie"].index("gazela")].split(" ")
        for index, bioma in enumerate(zoo_table["bioma"]):

            bioma = bioma.split(" ")

            # Calcula a diferença de animais no bioma, checa se tem tipo carnivoro, cria variável com a diferença de tamanho para diferentes espécies de cada animal
            animaisBioma = len(zoo_table["animais existentes"][index])
            contemCarnivoro = False

            if (animaisBioma > 0):
                
                for animalExistente in zoo_table["animais existentes"][index]:
                    if animalExistente in animaisCarnivoros:
                        contemCarnivoro = True
                    
                    if animalExistente == "gazela":
                        animaisBioma -= 1 

            for e in bioma:
                if (e in biomaAnimal and ((animaisBioma == 0) or (contemCarnivoro == False))):
                    if zoo_table["tamanho restante"][index] - animaisBioma >= tamanhoAnimal * quantidade:
                        print("Recinto {} (espaço livre: {} total: {}".format(index+1, zoo_table["tamanho restante"][index] - (tamanhoAnimal  * quantidade) - animaisBioma, zoo_table["tamanho total"][index]))
                    else:
                        print("Não há recinto viável")

    elif animal == "hipopotamo":
        tamanhoAnimal = animals_table["tamanho"][animals_table["especie"].index("hipopotamo")]
        biomaAnimal = animals_table["bioma"][animals_table["especie"].index("hipopotamo")].split(" ")
        
        # Hipopotamos só ficam em biomas do tipo savana e rio
        biomaAnimal.pop(1)
        for index, bioma in enumerate(zoo_table["bioma"]):
            bioma = bioma.split(" ")

            if (len(bioma) > 1):
                bioma.pop(1)
            if bioma != biomaAnimal:
                continue
            else:

                # Calcula a diferença de animais no bioma, checa se tem tipo carnivoro, cria variável com a diferença de tamanho para diferentes espécies de cada animal
                animaisBioma = len(zoo_table["animais existentes"][index])
                contemCarnivoro = False

                if (animaisBioma > 0):
                    
                    for animalExistente in zoo_table["animais existentes"][index]:
                        if animalExistente in animaisCarnivoros:
                            contemCarnivoro = True
                        
                        if animalExistente == "hipopotamo":
                            animaisBioma -= 1 

                for e in bioma:
                    if (e in biomaAnimal and ((animaisBioma == 0) or (contemCarnivoro == False))):
                        if zoo_table["tamanho restante"][index] - animaisBioma >= tamanhoAnimal * quantidade:
                            print("Recinto {} (espaço livre: {} total: {}".format(index+1, zoo_table["tamanho restante"][index] - (tamanhoAnimal  * quantidade) - animaisBioma, zoo_table["tamanho total"][index]))
                            break
                        else:
                            print("Não há recinto viável")
                            break
    else:
        print("Animal inválido")


entrada = input().split(",")
entrada[0] = entrada[0].replace('\"', '')
entrada[1] = entrada[1].replace(' ', '')
entrada[1] = int(entrada[1])
analisaRecintos(entrada[0], entrada[1])