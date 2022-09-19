#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# La base de datos que estaremos importando será de los pesos y las alturas
# de hombres y mujeres. Sin embargo, nosotros solo utilizaremos los datos
# de los hombre para el ejercicio, pues presentan mayor variación de datos.

df = pd.read_csv('./Estatura-peso_HyM.csv')
df1 = df
df = df[["H_estat","H_peso"]]

# ANtes de hacer el modelo haremos la separación de los datos
# Más o menos intente hacer una separación del 80% de los datos
# en los datos de entrenamiento y solo 20% de los datos van a la prueba.

X_prueba = df.iloc[0:175]
X_p = X_prueba[['H_peso']].values
y_p = X_prueba[['H_estat']].values

X_test = df.iloc[175:219]
X_t = X_test[['H_peso']].values
y_t = X_test[['H_estat']].values


X = df['H_peso']
y = df['H_estat']


# In[2]:


# Creación del modelo

X_media = X_p.mean()

xDif = X_media - X_p
xDif2 = xDif**2

Sxx = xDif2.sum()

y_media = y_p.mean()

yDif = y_media - y_p

Sxy = (xDif*yDif).sum()

m = Sxy/Sxx

b = y_media - m * X_media


# In[3]:


def prediccion(a):
    return m*a+b


# In[4]:


valor = input("Escribe un peso para calcular su estatura: ")
valor = float(valor)

print('La predicción de estatura con un peso de ',valor,' es : ')
print(round(prediccion(valor),2))
print('\n')


# In[5]:


listaP = []
for x in range(len(X_t)):
    a = float(prediccion(X_t[x]))
    listaP.append(a)


# In[6]:


plt.plot(X_t,listaP, 'co',label='Predicciones') #Los registros azules son las predicciones.
plt.plot(X_t,y_t,'ro', label='Originales') #Los registros originales están de color rojo.

plt.title("Gráfica de datos vs predicción")
plt.xlabel("Pesos")
plt.ylabel("Estaturas")

plt.figure()


# In[7]:


from sklearn.metrics import r2_score
r2_score(y_t,listaP)

# Usando una libreria para medir la precisión del modelo vemos que el modelo presenta un buen resultado.
