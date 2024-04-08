#--------------------------------------------------------------#
#----------------------------- EVPY ---------------------------#
#--------------------------------------------------------------#

import requests
import os

#---------------- PT-BR -----------------------------------

# Acesse https://isitarealemail.com e cadastre-se no site.
# Depois do cadastro ter sido feito, acesse: https://isitarealemail.com/getting-started/api
# e use a chave api no script. :)

# A chave API é para fim de testes, talvez eu a deixe no script.
# ---------------------------------------------------------

# ------------------ EN -----------------------------------
# 
# Visit https://isitarealemail.com and register on the site.
# After registration has been done, go to: https://isitarealemail.com/getting-started/api
# and use the api key in the script. :)

# The API key is for testing purposes, maybe I'll leave it in the script.

api_key = str(input("Digite sua chave api: "))

# Functions

def welcome():
	os.system('cls' if os.name == 'nt' else 'clear')
	print('''
		8 8888888888 `8.`888b           ,8' 8888888 8888888888 
		8 8888        `8.`888b         ,8'        8 8888       
		8 8888         `8.`888b       ,8'         8 8888       
		8 8888          `8.`888b     ,8'          8 8888       
		8 888888888888   `8.`888b   ,8'           8 8888       
		8 8888            `8.`888b ,8'            8 8888       
		8 8888             `8.`888b8'             8 8888       
		8 8888              `8.`888'              8 8888       
		8 8888               `8.`8'               8 8888       
		8 888888888888        `8.`                8 8888 
		\n   
	''')
	print("\n\t\t[1] EN (English)\n\t\t[2] PT-BR (Portuguese - Brazil)\n\t\t[3] exit | sair")



def email_indiv():
	try:
		if language == 1:
			email = str(input('\nEmail to verify -> '))
		elif language == 2:
			email = str(input('\nEmail para verificar -> '))

		response = requests.get(
		"https://isitarealemail.com/api/email/validate",
		params = {'email': email},
		headers = {'Authorization': "Bearer " + api_key}
		)

		status = response.json()['status']
		
		if language == 1:
			if status == "valid":
				print("\nThe email: %s is valid\n" % email)
			elif status == "invalid":
				print("\nThe email: %s is invalid\n" % email)
				email_indiv()
			else:
				print("\nThe email provided was not found\n")
				email_indiv()
		
		elif language == 2:
			if status == "valid":
				print("\nO email: %s é válido\n" % email)
			elif status == "invalid":
				print("\nO email: %s é inválido\n" % email)
				email_indiv()
			else:
				print("\nO email fornecido não foi achado\n")
				email_indiv()
		

	except KeyboardInterrupt:
		if language == 1:
			print("Until later ;)")
		elif language == 2:
			print('Até mais ;)')

def email_multip(name_list):
	result_email = {}
	try:
		with open(name_list, "r") as list:
			emails = list.read().split('\n')
			emails.remove('')
			for email in emails:
				response = requests.get(
				"https://isitarealemail.com/api/email/validate",
				params = {'email': email},
				headers = {'Authorization': "Bearer " + api_key}
				)
				status = response.json()['status']
			
				result_email[email] = status

			

			for email_address in result_email.keys():
				#if language == 1:
				print(email_address, ":", result_email[email_address])
				#elif language == 2:
					#if status == 'valid':
						#print("\nO email:", email_address, "é válido")
					#elif status == "invalid":
						#print("\nO email:", email_address, "é inválido")
	except KeyboardInterrupt:
		if language == 1:
			print("\nGoodbye !\n")
		elif language == 2:
			print("\nAté mais amigo cibernético ;D\n")
	
	if language == 1:
		print("\nGoodbye !\n")
	elif language == 2:
		print("\nAté mais amigo cibernético ;D")
				



def select_language(language):
	if language == 1:
		print('\n\t\t[1] analyze a single email\n\t\t[2] analyze multiple emails\n\t\t[3] = exit\n')
		cod = int(input('Type the code: '))
		select_code(cod)
	elif language == 2:
		print('\n\t\t[1] analisar um único email\n\t\t[2] analisar múltiplos emails\n\t\t[3] sair\n')
		cod = int(input('Digite o código: '))
		select_code(cod)
	elif language == 3:
		print('\nexiting | saindo \n')

def select_code(cod):
	if cod == 1:
		email_indiv()
	elif cod == 2:
		try:
			if language == 1:
				name_list = str(input("\nName of the email list -> "))
			elif language == 2:
				name_list = str(input("\nNome da lista de emails -> "))
			email_multip(name_list)
		except KeyboardInterrupt:
			if language == 1:
				print('Bye bye !')
			elif language == 2:
				print("ctrl + c \nAté mais, que a força esteja com você ;)")
	elif cod == 3:
		if language == 1:
			print('Goodbye!\n')
		elif language == 2:
			print('Até mais ! ^. .^ 			<-- Isso é um gato\n')

# --------------------------

try:
	welcome()
	language = int(input("\n--> "))
	select_language(language)
except KeyboardInterrupt:
	print("ctrl + c")






