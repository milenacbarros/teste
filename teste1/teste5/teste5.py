
def inverter_string(s):
    # slicing, começa no final da string e percorre ate o começo
    return s[::-1]

# entrada
texto = input("Digite uma string para inverter: ")

print("Texto invertido:", inverter_string(texto))
