import time
import random


Inspermons = {

			"Clayton": {"Poder de ataque":55, "Nível de Defesa": 15,"Pontos de Vida":100},
			"Robson":{"Poder de ataque": 70, "Nível de Defesa":15,"Pontos de Vida":100},
			"Wilson":{"Poder de ataque":60,"Nível de Defesa":10,"Pontos de Vida":100},
			"Weirdelas":{"Poder de ataque":65,"Nível de Defesa":17,"Pontos de Vida":100},
			"Carlos":{"Poder de ataque":75,"Nível de Defesa":12,"Pontos de Vida":100},
			"Isimon":{"Poder de ataque":72,"Nível de Defesa":16,"Pontos de Vida":100},
			"Dududelas":{"Poder de ataque":71,"Nível de Defesa":18,"Pontos de Vida":100},
			





			}

listafound = ["Clayton","Robson"]
Insperdex = []
sorte = [0.2,0.5,1,1.1,1.2,1.4,1.8]
fugaoubatalha = [1,2]

def Batalha(nome,poke):
	vidapoke = Inspermons[poke]['Pontos de Vida']
	vidanome = Inspermons[nome]['Pontos de Vida']
	ataquepoke = Inspermons[poke]['Poder de ataque']
	ataquenome = Inspermons[nome]['Poder de ataque']
	defesapoke = Inspermons[poke]['Nível de Defesa']
	defesanome = Inspermons[nome]['Nível de Defesa']
	s = int(random.choice(sorte))
	x = int(random.choice(sorte))
	fuga = int(input("Deseja fugir ou batalhar? Digite 1 para fugir e 2 para batalhar"))

	if fuga == 1:
		fb = int(random.choice(fugaoubatalha))
		print(fb)
		if fb == 1:
			while vidapoke>0 and vidanome>0:
				print("Sua fuga não foi bem sucedida! Você perdeu 1 round de ataque!")

				vidanome = vidanome - ((ataquepoke - defesanome)*x)
				print(x)
				print("A vida do seu adversário foi reduzida para {0}".format(vidanome))
				if vidanome <= 0:
					print("Você venceu!")
					time.sleep(2)
					break


				vidapoke = vidapoke - ((ataquenome - defesapoke)*s)
				print(s)
				print("Sua vida foi reduzida para {0}".format(vidapoke))
				time.sleep(2)		
				if vidapoke <= 0:
					print("Você perdeu!")
					time.sleep(2)
					print("Até o próximo jogo!")
					time.sleep(3)
					break
		if fb == 2:
			time.sleep(2)
			print("Você fugiu! Até a próxima batalha!")
		
		
			
				


		
	
	


	




t = 10000000000000
for i in range(t):
	print("Olá seja bem vindo ao Inspermon! Escolha um entre os seguintes inspermons! Carlos,Clayton,Robson, Weirdelas, Isimon, Dududelas")
	time.sleep(1)
	poke = input("Qual bichano você deseja!? ")
	
	if poke not in Inspermons:
		print("Tente novamente!Escolha um Inspermon entre os disponíveis! Letra maiuscula e miniscula são levadas em consideração!")
		time.sleep(2)
		break
	if poke in Inspermons:
		print("Muito bem! Você selecionou o {0} e seus atributos são: Pontos de Vida: {1}, Poder de Ataque: {2} e Nível de Defesa: {3}".format(poke,Inspermons[poke]['Pontos de Vida'],Inspermons[poke]['Poder de ataque'],Inspermons[poke]['Nível de Defesa']))
	time.sleep(1)

	poud = int(input("O que deseja fazer? Passear ou Dormir? Digite 1 para Passear e 2 para Dormir: "))
	if poud == 2:
		print("Beleza! Vamos dormir!")
		break
		time.sleep(10)
	if poud == 1:
		time.sleep(1)
		print("Ok! Vamos lá!")
		time.sleep(1)
		nome = str(random.choice(listafound))
		Insperdex.append(nome)
		Insperdex.append(Inspermons[nome]["Pontos de Vida"])
		print("Ora ora, você encontrou um Inspermon Selvagem ele é o {0} e seus atributos são: Pontos de Vida: {1}, Poder de Ataque: {2} e Nível de Defesa: {3}".format(nome,Inspermons[nome]['Pontos de Vida'],Inspermons[nome]['Poder de ataque'],Inspermons[nome]['Nível de Defesa']))
		time.sleep(2)
		print("Sua batalha vai começar!")
		time.sleep(2)
		Batalha(nome,poke)

			


		print(Insperdex)
	


		












