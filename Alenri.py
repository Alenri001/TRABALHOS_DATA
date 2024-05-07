import pandas as pd

dados = {'nome': ['Angel','javid','aloizio','alenri'],
      'idade' : [17,18,20,17],
      'departamento' : ['administrativo','financeiro','comercial','produção'],
      'salario' : [34000,22000,50000,20000]}

df = pd.DataFrame(dados)

print(df)


dados = df ['departamento']
print(dados.info())
print(dados)


df['salario_definitivo'] = df ['salario'] * 4
print(df)


import matplotlib.pyplot as plt





plt.plot(df['nome'],(df['salario']))

plt.title('grafico de linha simples')
plt.xlabel('eixo x')
plt.ylabel('eixo y')

plt.show()



