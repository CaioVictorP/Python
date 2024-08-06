o = 0
i = 0
menimc = float(9999999)
mennome = ""
maiimc = -1
mainome = ""
imcty = ""
nome = input("Digite o nome do cidadão: ")
listanome = []
listanome.append(nome)
alt = float(input("Digite a altura do cidadão: "))
listaalt = []
listaalt.append(alt)
peso = float(input("Digite o peso do cidadão: "))
listapeso = []
listapeso.append(peso)
imc = peso / alt ** 2
listaimc = []
listaimc.append(imc)
if menimc > imc:
	menimc = imc
	mennome = nome
if maiimc < imc:
	maiimc = imc
	mainome = nome
for i in range(50):
	nome = input("Digite o nome do cidadão: ")
	listanome.append(nome)
	alt = float(input("Digite a altura do cidadão: "))
	listaalt.append(alt)
	peso = float(input("Digite o peso do cidadão: "))
	listapeso.append(peso)
	imc = peso / alt ** 2
	listaimc.append(imc)
	if menimc > imc:
		menimc = imc
		mennome = nome
	if maiimc < imc:
		maiimc = imc
		mainome = nome
for o in range(50):
	if listaimc[o] <= 18.5:
		imcty = " peso abaixo do normal"
	elif listaimc[o]  > 18.5 and listaimc[o] < 25:
		imcty = " peso normal"
	elif listaimc[o] >= 25 and listaimc[o] < 30:
		imcty = " Sobrepeso"
	elif listaimc[o] >= 30 and listaimc[o] < 35:
		imcty = "a obesidade grau I"
	elif listaimc[o] >= 35 and listaimc[o] < 40:
		imcty = "a obesidade grau II"
	else:
		imcty = "a obesidade grau III"
	print(f"O cidadão de nome {listanome[o]} tem um IMC de {listaimc[o]:.1f}, estando com um{imcty}")
if maiimc <= 18.5:
	imcty = " peso abaixo do normal"
	print(f"O cidadão de nome {mainome} tem o maior IMC de {maiimc:.1f}, estando com um{imcty}")
elif maiimc > 18.5 and maiimc < 25:
	imcty = " peso normal"
	print(f"O cidadão de nome {mainome} tem o maior IMC de {maiimc:.1f}, estando com um{imcty}")
elif maiimc >= 25 and maiimc < 30:
	imcty = " Sobrepeso"
	print(f"O cidadão de nome {mainome} tem o maior IMC de {maiimc:.1f}, estando com um{imcty}")
elif maiimc >= 30 and maiimc < 35:
	imcty = "a obesidade grau I"
	print(f"O cidadão de nome {mainome} tem o maior IMC de {maiimc:.1f}, estando com um{imcty}")
elif maiimc >= 35 and maiimc < 40:
	imcty = "a obesidade grau II"
	print(f"O cidadão de nome {mainome} tem o maior IMC de {maiimc:.1f}, estando com um{imcty}")
else:
	imcty = "a obesidade grau III"
	print(f"O cidadão de nome {mainome} tem o maior IMC de {maiimc:.1f}, estando com um{imcty}")

if menimc <= 18.5:
	imcty = " peso abaixo do normal"
	print(f"O cidadão de nome {mennome} tem o menor IMC de {menimc:.1f}, estando com um{imcty}")
elif menimc > 18.5 and menimc < 25:
	imcty = " peso normal"
	print(f"O cidadão de nome {mennome} tem o menor IMC de {menimc:.1f}, estando com um{imcty}")
elif menimc >= 25 and menimc < 30:
	imcty = " Sobrepeso"
	print(f"O cidadão de nome {mennome} tem o menor IMC de {menimc:.1f}, estando com um{imcty}")
elif menimc >= 30 and menimc < 35:
	imcty = "a obesidade grau I"
	print(f"O cidadão de nome {mennome} tem o menor IMC de {menimc:.1f}, estando com um{imcty}")
elif menimc >= 35 and menimc < 40:
	imcty = "a obesidade grau II"
	print(f"O cidadão de nome {mennome} tem o menor IMC de {menimc:.1f}, estando com um{imcty}")
else:
	imcty = "a obesidade grau III"
	print(f"O cidadão de nome {mennome} tem o menor IMC de {menimc:.1f}, estando com um{imcty}")