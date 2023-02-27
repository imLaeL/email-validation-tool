#--------------------------------------------------------------#
#----------------------------- EVPY ---------------------------#
#--------------------------------------------------------------#

import requests

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

api_key = '4a6bddfb-fbdf-41b4-9e96-34de7d23d5b5'


print("\t\t[1] EN (English)\n\t\t[2] PT-BR (Portuguese - Brazil)")

try:
	language = int(input("--> "))
except KeyboardInterrupt:
	print("ctrl + c")

def email_indiv():
	try:
		email = str(input('\nEmail para verificar -> '))

		response = requests.get(
		"https://isitarealemail.com/api/email/validate",
		params = {'email': email},
		headers = {'Authorization': "Bearer " + api_key}
		)

		status = response.json()['status']

		if language == 1:
			if status == "valid":
				print("\nO email: %s é válido\n" % email)
			elif status == "invalid":
				print("\nO email: %s é inválido\n" % email)
				email_indiv()
			else:
				print("\nO email fornecido não foi achado\n")
				email_indiv()
		elif language == 2:
			if status == "valid":
				print("\nThe email: %s is valid\n" % email)
			elif status == "invalid":
				print("\nThe email: %s is invalid\n" % email)
				email_indiv()
			else:
				print("\nThe email provided was not found\n")
				email_indiv()

	except KeyboardInterrupt:
		if language == 1:
			print("Until later ;)")
		elif language == 2:
			print('Até mais ;)')

if language == 1:
	print('cod 1 = analyze a single email\ncod 2 = analyze multiple emails\ncod 3 = exit\n')
	cod = int(input('Type the code: '))

elif language == 2:
	print('cod 1 = analisar um único email\ncod 2 = analisar múltiplos emails\ncod 3 = sair\n')
	cod = int(input('Digite o código: '))


if cod == 1:
	email_indiv() 
#elif cod == 2:		--> Coming Soon
	#email_multip()
elif cod == 3:
	if language == 1:
		print('Goodbye!')
	elif language == 2:
		print('Até mais ^. .^ <- Isto é um gato')

