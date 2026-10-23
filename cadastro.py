pessoa = {'nome': 'Kalita', 'idade': 25, 'cidade': 'Florianópolis', 'profissão': 'fotógrafa'}
print(pessoa)
pessoa.update({'email':'maelly@gmail.com'})
print(pessoa)

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
    
