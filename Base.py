#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report

import sklearn.metrics as metrics
from sklearn.model_selection import learning_curve


#Leemos el archivo .xlxs
df2=pd.read_excel('E-Commerce_train.xlsx')


#Creamos una copia del dataframe original
df=df2.copy()


# Quitamos la columna ID y Gender y asignamos la columna "target"

X=df
X.rename({'Reached.on.Time_Y.N':'target'}, axis=1, inplace=True)
y=X['target']
X=df.drop(columns=['ID','Gender','target'])



# Analizando el dataframe, tenemos cuatro campos con valores tipo str que habrá que codificar para poder procesarlos.

# Procesamos estos campos con LaberEncoder para obtener un dataframe codificado


from sklearn.preprocessing import LabelEncoder

#Shipment (Flight=0, road=1 o ship=2)

Shipment=X['Mode_of_Shipment'].values
enc=LabelEncoder().fit(Shipment)

Shipment=enc.transform(Shipment)
Shipment=pd.DataFrame(Shipment)

X.drop(columns="Mode_of_Shipment", inplace=True)
X.insert(1,'Mode_of_Shipment', Shipment)


#Warehouse_block (D=3,F=4,A=0,B=1,C=2)

Warehouse_block=X['Warehouse_block'].values
enc=LabelEncoder().fit(Warehouse_block)

Warehouse_block=enc.transform(Warehouse_block)
Warehouse_block=pd.DataFrame(Warehouse_block)

X.drop(columns="Warehouse_block", inplace=True)
X.insert(0,'Warehouse_block', Warehouse_block)


#Product_importance (low=1, medium=2, high=0)

Product_importance=X['Product_importance'].values
enc=LabelEncoder().fit(Product_importance)

Product_importance=enc.transform(Product_importance)
Product_importance=pd.DataFrame(Product_importance)

X.drop(columns="Product_importance", inplace=True)
X.insert(6,'Product_importance', Product_importance)




# Escalamos (Estandarizamos y luego normalizamos).

columnas_testeo = ['Cost_of_the_Product','Discount_offered', 'Weight_in_gms']
X_ajustar = X[columnas_testeo]


# Normalizamos con MinMaxScaler
X_scaled = MinMaxScaler().fit_transform(X_ajustar) # Scale the features

X_scaled=pd.DataFrame(X_scaled)

X_scaled.rename({0:'Cost_of_the_Product',1:'Discount_offered',2:'Weight_in_gms'}, axis=1, inplace=True)



#Concatenamos las celdas normalizadas y el resto del df
X1=X_scaled
X2=X.drop(columns=['Cost_of_the_Product','Discount_offered', 'Weight_in_gms'])
X=pd.concat([X1,X2],axis=1)




#Separamos nuestra data en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify = y)



# Vamos a balancear nuestro dataset con un sobremuestreo de la clase minoritaria, es decir de las veces que no se entregó el paquete, con el algoritmo SMOTE.
#Esto es para over_sampling

from imblearn import over_sampling
from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=2)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train.ravel())
print('After OverSampling, the shape of train_X: {}'.format(X_train_res.shape)) 
print('After OverSampling, the shape of train_y: {} \n'.format(y_train_res.shape)) 
  
print("After OverSampling, counts of label '1': {}".format(sum(y_train_res == 1))) 
print("After OverSampling, counts of label '0': {}".format(sum(y_train_res == 0)))


