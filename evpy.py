import requests
import os

# Função de boas-vindas
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
    print("\n\t\tCriado por imLaeL\n")
    print("\n\t1. Verificar um e-mail\n\t2. Verificar uma lista de e-mails\n")

# Função para verificar um e-mail individual
def email_indiv(api_key):
    try:
        email = input("Digite o email para validar: ")

        # Endpoint da API
        url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"

        # Fazendo a requisição GET
        response = requests.get(url)

        # Processando a resposta
        if response.status_code == 200:
            data = response.json()
            if data["data"]["result"] == "deliverable":
                print(f"O e-mail '{email}' é válido.")
            else:
                print(f"O e-mail '{email}' NÃO é válido.")
        else:
            print(f"Erro na requisição. Status code: {response.status_code}, Detalhes: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao realizar a requisição: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Função para verificar uma lista de e-mails
def email_list(api_key):
    try:
        file_path = input("Digite o caminho do arquivo contendo a lista de e-mails: ")

        if not os.path.exists(file_path):
            print("O arquivo não existe.")
            return

        with open(file_path, "r") as file:
            emails = [email.strip() for email in file.readlines() if email.strip()]

        for email in emails:
            url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if data["data"]["result"] == "deliverable":
                    print(f"O e-mail '{email}' é válido.")
                else:
                    print(f"O e-mail '{email}' NÃO é válido.")
            else:
                print(f"Erro na requisição. Status code: {response.status_code}, Detalhes: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao realizar a requisição: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Função principal
def main():
    try:
        api_key = input("Digite sua chave API: ").strip()
        
        if not api_key:
            print("Você precisa fornecer uma chave de API válida.")
            return

        welcome()
        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite apenas números.")
            return

        if option == 1:
            email_indiv(api_key)
        elif option == 2:
            email_list(api_key)
        else:
            print("Opção inválida.")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")

# Executa o programa
if __name__ == "__main__":
    main()
