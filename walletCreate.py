from eth_account import Account

def create_wallets(num_wallets):
    wallets = []
    private_keys = []
    
    for _ in range(num_wallets):
        
        account = Account.create()
        
        
        address = account.address
        private_key = account._private_key.hex()
        

        wallets.append(f"{address},0.021")
        private_keys.append(f"{{ pk: \"{private_key}\" }},")
    
    return wallets, private_keys

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

if __name__ == "__main__":
    num_wallets = 500 # Coloque aqui o numero de walllets que deseja ser criada
    
    
    wallets, private_keys = create_wallets(num_wallets)
    

    save_to_file("wallets.txt", wallets)
    

    save_to_file("private_keys.txt", private_keys)

    print("Arquivos wallets.txt e private_keys.txt gerados com sucesso.")
