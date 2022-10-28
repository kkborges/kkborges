def ler_token() -> str:
    with open("token.txt", "r",) as arquivo:
        token = arquivo.read()
    return str(token)

token:str=ler_token()
