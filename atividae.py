# Desenvolva um programa em Python que determine se um determinado ano é bissexto ou não, levando em consideração as regras do calendário gregoriano. Além disso, seu programa deve fornecer uma explicação detalhada do motivo pelo qual o ano é ou não é bissexto, com base nas seguintes condições:

# Um ano é bissexto se for divisível por 4, exceto quando também for divisível por 100, a menos que seja divisível por 400.
# Caso o ano seja bissexto, deve-se explicar que ele possui 366 dias.
# Se o ano não for bissexto, deve-se explicar que ele possui 365 dias.
# O programa deve solicitar ao usuário que insira o ano desejado e, em seguida, fornecer a resposta juntamente com a explicação correspondente.
# Lembre-se de incluir mensagens informativas e claras para orientar o usuário durante a interação com o programa.

# O código deve estar comentado de forma a que possa explicar suas ações,

def eh_bissexto(ano):
    # Verifica se o ano é divisível por 4
    if ano % 4 == 0:
        # Verifica se o ano é divisível por 100 e não é divisível por 400
        if ano % 100 == 0 and ano % 400 != 0:
            return False, "O ano não é bissexto, pois é divisível por 100, mas não por 400."
        else:
            return True, "O ano é bissexto, pois é divisível por 4 e, se divisível por 100, também é divisível por 400."
    else:
        return False, "O ano não é bissexto, pois não é divisível por 4."

# Função para obter a explicação
def explicacao_bissexto(ano, bissexto):
    if bissexto:
        return f"O ano {ano} é bissexto e possui 366 dias."
    else:
        return f"O ano {ano} não é bissexto e possui 365 dias."

# Solicita ao usuário que insira o ano
ano = int(input("Digite o ano que você deseja verificar se é bissexto: "))

# Verifica se o ano é bissexto e obtém a explicação correspondente
bissexto, explicacao = eh_bissexto(ano)

# Imprime o resultado e a explicação
print(explicacao_bissexto(ano, bissexto))
print("Explicação:", explicacao)
