i = 0
o = 0
menpeso = 9999999
mennum = 0
maipeso = -1
mainum = 0
gado = float(input("Digite o peso do gado: "))
lista = []
lista.append(gado)
if menpeso > gado:
    menpeso = gado
    mennum = i + 1
if maipeso < gado:
    maipeso = gado
    mainum = i + 1
i += 1
condition = input("Caso deseja terminar, aperte ENTER ")
if (condition != ""):
    gado = float(input("Digite o peso do gado: "))
    while True:
        lista.append(gado)
        if menpeso > gado:
            menpeso = gado
            mennum = i + 1
        if maipeso < gado:
            maipeso = gado
            mainum = i + 1
        i += 1
        try:
            gado = float(input("Digite o peso do gado: "))
        except ValueError:
            break
for o in range(i):
    print(f"O gado número {o + 1} tem um peso de {lista[o]}kg")
if i >= 2:
    print(f"O gado mais leve é o número {mennum}, com um peso de {menpeso}kg")
    print(f"O gado mais pesado é o número {mainum}, com um peso de {maipeso}kg")