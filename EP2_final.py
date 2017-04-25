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
		

			} #dicionario com os Inspermons




listafound = ["Clayton","Robson","Wilson","Weirdelas","Carlos","Isimon","Dududelas"]
Insperdex = [] #Insperdex que é completa a cada rodada com o novo Inspermon
sorte = [0.2,0.5,1,1.1,1.2,1.4,1.8] # Valores que influenciam a batalha "sorte"
fugaoubatalha = [1,2] # Valores para aleatóriamente validar ou não a fuga

def Batalha(nome,poke): # função batalha
	vidapoke = Inspermons[poke]['Pontos de Vida']
	vidanome = Inspermons[nome]['Pontos de Vida']
	ataquepoke = Inspermons[poke]['Poder de ataque']
	ataquenome = Inspermons[nome]['Poder de ataque']
	defesapoke = Inspermons[poke]['Nível de Defesa']
	defesanome = Inspermons[nome]['Nível de Defesa']
	s = int(random.choice(sorte)) #selecionar um valor como sorte
	x = int(random.choice(sorte)) #selecionar outro valor como sorte
	fuga = int(input("Deseja fugir ou batalhar? Digite 1 para fugir e 2 para batalhar"))

	if fuga == 1: #validando a fuga
		fb = int(random.choice(fugaoubatalha))
		print(fb)
		if fb == 1: #se a fuga não der certo você perde uma rodada
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
		if fb == 2: #se funcionar você foge
			time.sleep(2)
			print("Você fugiu! Até a próxima batalha!")
		
		
			
				


	if fuga == 2: #se você opta por batalhar
		while vidapoke>0 and vidanome>0:
	
			vidapoke = vidapoke - ((ataquenome - defesapoke)*s)
			print("Sua vida foi reduzida para {0}".format(vidapoke))
			time.sleep(2)	


			if vidapoke <= 0:
				print("Você perdeu!")
				time.sleep(2)
				print("Até o próximo jogo!")
				time.sleep(3)
				break
		
			
			vidanome = vidanome - ((ataquepoke - defesanome)*x)
			print("A vida do seu adversário foi reduzida para {0}".format(vidanome))

			if vidanome <= 0:
				print("Você venceu!")
				time.sleep(2)
				break
	



t = 10000000000000

for i in range(t):
	nome = str(random.choice(listafound))
	print("Olá seja bem vindo ao Inspermon! Escolha um entre os seguintes inspermons! Carlos,Clayton,Robson, Weirdelas, Isimon, Dududelas")
	time.sleep(1)
	poke = input("Qual bichano você deseja!? ")
	
	if poke not in Inspermons: #se você optar por um nome que não existe no dicionario
		print("Tente novamente!Escolha um Inspermon entre os disponíveis! Letra maiuscula e miniscula são levadas em consideração!")
		time.sleep(2)
		break
	if poke in Inspermons:
		print("Muito bem! Você selecionou o {0} e seus atributos são: Pontos de Vida: {1}, Poder de Ataque: {2} e Nível de Defesa: {3}".format(poke,Inspermons[poke]['Pontos de Vida'],Inspermons[poke]['Poder de ataque'],Inspermons[poke]['Nível de Defesa']))
	time.sleep(1)

	poud = int(input("O que deseja fazer? Passear ou Dormir? Digite 1 para Passear,2 para Dormir e 3 para vizualizar a sua Insperdex!: "))
	if poud == 3:
		print(Insperdex)
		if Insperdex == []:
			print("Você ainda não encontrou nenhum Inspermon Selvagem! Recomece o jogo e vá em busca do seu!")

	if poud == 2:
		print("Beleza! Vamos dormir!")
		break
		time.sleep(10)
	if poud == 1:
		time.sleep(1)
		print("Ok! Vamos lá!")
		time.sleep(1)
		
		print("Ora ora, você encontrou um Inspermon Selvagem ele é o {0} e seus atributos são: Pontos de Vida: {1}, Poder de Ataque: {2} e Nível de Defesa: {3}".format(nome,Inspermons[nome]['Pontos de Vida'],Inspermons[nome]['Poder de ataque'],Inspermons[nome]['Nível de Defesa']))
		time.sleep(2)
		print("Sua batalha vai começar!")
		time.sleep(2)
		Batalha(nome,poke)
		if nome not in Insperdex:
			Insperdex.append(nome)
			Insperdex.append(Inspermons[nome]['Pontos de Vida'])
			Insperdex.append(Inspermons[nome]['Poder de ataque'])
			Insperdex.append(Inspermons[nome]['Nível de Defesa'])	

		
	


		












