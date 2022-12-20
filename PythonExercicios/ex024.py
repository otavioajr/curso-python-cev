cidade = str(input('Digite o nome de sua cidade: '))
dividido = cidade.upper().split()
print(dividido[0] == 'SANTO')

##### RESOLUÇÃO DO PROFESSOR #####

cid = str(input('Digite a cidade onde nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')