
# fonction qui permet de générer le code de la mission grâce à un dictionnaire
# il va concatener les clés et les valeurs
def mission_code(code_dict):
    mission_code = ''
    for letter, number in code_dict.items():
        mission_code += (letter + str(number))
    return mission_code


# fonction qui permet de générer un diction grâce à une liste de nom
# la clé du dictionnaire sont les n premier caractère
# et la valeur est le nombre restant si on soustrait n à la taille du nom

def code_dictionnary(name_list):
    code_dict = dict()
    for j in range(len(name_list)):
        name_code = ''
        not_exist = True
        name = name_list[j].capitalize()
        rest_length = len(name)
        for i in range(len(name)):
            if not_exist:
                name_code += name[i]
                rest_length -= 1
                not_exist = code_dict.__contains__(name_code)
            else:
                break
        code_dict[name_code] = rest_length

    return code_dict

