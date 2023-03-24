# cria lista de códigos Unicode a partir de uma string

# usando lista comum
simbolos = '$¢£¥€ê'
codigos = []

for simbolo in simbolos:
    codigos.append(ord(simbolo))


print(codigos)


# usando list comprehensions

simbolos = '$¢£¥€ê'
codigos = [ord(simbolo) for simbolo in simbolos]
print(codigos)

# qual exemplo é mais fácil de ler?