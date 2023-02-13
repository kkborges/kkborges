def ler_token():
    with open("token.txt", "r",) as arquivo:
        token = arquivo.read()
    return token
