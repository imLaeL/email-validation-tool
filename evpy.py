#--------------------------------------------------------------#
#----------------------------- EVPY ---------------------------#
#--------------------------------------------------------------#

import requests

# Acesse https://isitarealemail.com e cadastre-se no site.
# Depois do cadastro ter sido feito, acesse: https://isitarealemail.com/getting-started/api
# e use a chave api no script. :)

api_key = '4a6bddfb-fbdf-41b4-9e96-34de7d23d5b5'

def email_indiv():
	try:
		email = str(input('\nEmail para verificar -> '))

		response = requests.get(
		"https://isitarealemail.com/api/email/validate",
		params = {'email': email},
		headers = {'Authorization': "Bearer " + api_key}
		)

		status = response.json()['status']

		if status == "valid":
			print("\nO email: %s é válido\n" %email)
		elif status == "invalid":
			print("\nO email: %s é inválido\n" %email)
			email_indiv()
		else:
			print("\nO email fornecido não foi achado\n")
			email_indiv()

	except KeyboardInterrupt:
		print('Até mais ;)')

print('cod 1 = analisar um único email\ncod 2 = analisar múltiplos emails\ncod 3 = sair')

cod = int(input('Digite o código: '))

if cod == 1:
	email_indiv()
#elif cod == 2:
	#email_multip()
elif cod == 3:
	print('até mais ;)')

