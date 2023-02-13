#--------------------------------------------------------------#
#----------------------------- EVPY ---------------------------#
#--------------------------------------------------------------#

import requests

# Acesse https://isitarealemail.com e cadastre-se no site.
# Depois do cadastro ter sido feito, acesse: https://isitarealemail.com/getting-started/api
# e use a chave api no script. :)

api_key = str(input('\nChave API -> '))

email = str(input('\nEmail para verificar -> '))

response = requests.get(
	"https://isitarealemail.com/api/email/validate",
	params = {'email': email},
	headers = {'Authorization': "Bearer " + api_key})

status = response.json()['status']

if status == "valid":
	print("\nO email: %s é válido\n" %email)

elif status == "invalid":
	print("\nO email: %s é inválido\n" %email)

else:
	print("\nO email fornecido não foi achado\n")
