import pandas as pd
import matplotlib.pyplot as plt

# ...existing code...


# Escapando as barras invertidas
df = pd.read_excel('data/Morbidade_Hospitalar_do_SUS_CID_RJ.xlsx')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Converter a coluna 'data' para datetime se ainda não estiver
df['Data'] = pd.to_datetime(df['Data'])

# Agrupar os dados por mês e somar as internações
df.set_index('Data', inplace=True)
serie_temporal = df.resample('ME').sum()  # Resample mensal

# Criar o gráfico de linha
plt.figure(figsize=(12, 6))
plt.plot(serie_temporal.index, serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'], label='Internações', color='red')
plt.title('Série Temporal de Internações Hospitalares')
plt.xlabel('Data')
plt.ylabel('Número de Internações')
plt.grid()
plt.legend()
plt.show()

media_geral = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].mean()
print(f'Média Geral das Internações: {media_geral:.2f}')

media_por_ano = serie_temporal.resample('YE').mean()
print(media_por_ano['Morbidade_Hospitalar_do_SUS_RJ'])

mediana = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].median()
print(f'Mediana das Internações: {mediana:.2f}')

variancia = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].var()
print(f'Variância das Internações: {variancia:.2f}')

# Calcular o desvio padrão
desvio_padrao = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].std()
print(f'Desvio Padrão das Internações: {desvio_padrao:.2f}')

# Calcular o coeficiente de variação
coef_variacao = desvio_padrao / serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].mean()
print(f'Coeficiente de Variação das Internações: {coef_variacao:.2%}')  # Exibindo como porcentagem

# Calcular o mínimo
minimo = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].min()
print(f'Mínimo das Internações: {minimo}')

# Calcular o máximo
maximo = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].max()
print(f'Máximo das Internações: {maximo}')

# Calcular a assimetria
assimetria = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].skew()
print(f'Assimetria das Internações: {assimetria:.2f}')

# Calcular a curtose
curtose = serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'].kurtosis()
print(f'Curtose das Internações: {curtose:.2f}') 

# Cálculo da probabilidade
faixa_inferior = 5000
faixa_superior = 15000

# Contar o número total de meses
total_meses = serie_temporal.shape[0]

# Contar o número de meses na faixa especificada
meses_na_faixa = serie_temporal[(serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'] >= faixa_inferior) & 
                                 (serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'] <= faixa_superior)].shape[0]

# Calcular a probabilidade
probabilidade_faixa = meses_na_faixa / total_meses
print(f'Probabilidade dos valores mensais caírem entre {faixa_inferior} e {faixa_superior}: {probabilidade_faixa:.2%}')
p_a = serie_temporal[serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'] > 12000].shape[0] / total_meses
p_b = serie_temporal[serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'] > 10000].shape[0] / total_meses
p_b_a = serie_temporal[(serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'] > 10000) & 
                       (serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'] > 12000)].shape[0] / \
        serie_temporal[serie_temporal['Morbidade_Hospitalar_do_SUS_RJ'] > 12000].shape[0]

# ...existing code...

p_a_b = (p_b_a * p_a) / p_b
print(f'Probabilidade condicional P(A|B): {p_a_b:.2%}')
