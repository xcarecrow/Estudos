print(30*"*")
print('Bem vindo ao Restaurante do Ricardo!')
print(30*'*')

print('\n')

print('[1] - almoço')
print('[2] - sobremesas')
print('[3] - lanches')
print('[4] - bebidas')

print('\n')

a = input('Qual a sua pedido?\n:>')

print('\n')
print('\n')

almoco_lista = [('Feijoada', '$35,00'), ('file com fritas', '$23,00'), ('file de frango', '$17,00')]
sobremesas_lista = [('Sorvete', '$10,00'), ('torta de limão', '$7,00'), ('milk shake', '$15,00')]
lanches_lista = [('x-egg', '$8,00'), ('x-bacon', '$10,00'), ('x-salada', '$12,00')]
bebidas_lista = [('Suco natural', '$7,00'), ('refrigerante', '$5,00'), ('agua', '$3,00')]

print('Nos temos essas opções hoje:\n')

if a == '1':
	print(almoco_lista[0][0])
	print('\n')
	print(almoco_lista[1][0])
	print('\n')
	print(almoco_lista[2][0])

if a == '2':
	print(sobremesas_lista[0][0])
	print('\n')
	print(sobremesas_lista[1][0])
	print('\n')
	print(sobremesas_lista[2][0])
	
if a == '3':
	print(lanches_lista[0][0])
	print('\n')
	print(lanches_lista[1][0])
	print('\n')
	print(lanches_lista[2][0])

if a == '4':
	print(bebidas_lista[0][0])
	print('\n')
	print(bebidas_lista[1][0])
	print('\n')
	print(bebidas_lista[2][0])
