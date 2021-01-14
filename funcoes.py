import json
def registerJson(dados):
    with open("json.json", 'r') as j:
        arrayCadastrados = json.loads(j.read())
    arrayCadastrados.append(dados)
    with open('json.json', 'w') as json_file:
        json.dump(arrayCadastrados, json_file,indent=4)

def alterJson(dados):
    with open('json.json', 'w') as json_file:
        json.dump(dados, json_file,indent=4)

def getTable():
    with open("json.json", 'r') as j:
        contents = json.loads(j.read())
    return contents


##Validação do registro
def valid_register(name,lastname,value):
    try:
        value = int(value)
        
        if type(name) == str and type(lastname) == str and type(value) == int:
            return True
        else:
            return False
    except:
        return False


def forPorcent():
    json = getTable()
    totalSum = 0
    ##Adicionando o numero de unidades totais
    for row in json:
        totalSum += int(row["participation"])
    #Convertendo a lista em porcentagem
    for row in json:
        row["participation"] = str(round(((int(row["participation"])/totalSum)*100),2))+"%"
    return json

