<img src = "https://i0.wp.com/silverbirddelivery.com/wp-content/uploads/2021/06/Silverbird-White-Canva-Skewed.png?fit=500%2C500&ssl=1" height =300>

## **PROYECTO INDIVIDUAL 2 -DTS03 (DATATHON)**
# *Jhovany Lara Nava*

Para este proyecto individual, somos parte de un portal importante de E-commerce, el cual necesita hacer una predicción con la mejor métrica posible, que nos permita saber si un envío llegará a tiempo o no. Tenemos información contenida en un dataset, con los registros de diferentes envíos, con su respetiva efectividad, es decir si llegó a tiempo o no. Además se nos provee otro dataset con nuevos registros, con el bjetivo que nosotros hagamos una predicción y luego evaluemos el desempeño (Esa evauación la hace Henry, porque solo ellos tienen la respuesta).

Como método de evaluación del desempeño del modelo, se utilizará Exhaustividad (Recall) de la matriz de confusión (Confusion Matrix)


$  Recall=\frac{TP}{TP+FN} $ 

siendo $TP$ los verdaderos positivos, $TN$ verdaderos negativos y $FN$ los falsos negativos.

# 

`Procedimiento de solución`

Lo primero que hicimos, fué mirar la información y analizar qué tipo de datos tenemos, cuántos campos son, cuantos registros, calidad de la información, etc.
<img src ="https://c8.alamy.com/zooms/9/d432510925d44ae9ae21645a0991a371/k0y811.jpg" height= 300>

De allí trazamos nuestra línea de acción:

- Al tener campos categóricos, los procesamos con `LabelEnconder`.
- Quitamos los campos que no aportan a la predicción (ID y Gender). 
- `Normalizamos` aquellos campos que tengan valores muy elevados.
- Separamos nuestro dataset en entrenamiento y testeo.
- `Balanceamos` nuestras variables de entrenamiento.
- Elegimos el mejor modelo para predecir nuestro dataset.
- Finalmente lo entrenamos con Random Forest y lo `"testeamos"` para conocer su efectividad.

--> El proceso aplicado está en el archivo [Datathon Jhovany](Base.py); Ahí se hicieron los primeros 5 pasos.

--> Los últimos 2 pasos, se encuentran en el archivo [Datathon Jhovany](Modelos.ipynb).

Ojo, para que funcione el archivo Modelos.ipynb, primero se debe correr el archivo Base.py

La razón de separarlo, es para no volver a recorrer todo el script cada vez que muevo un parámetro o cada vez que pruebo un nuevo modelo.

#

Ahora hay que utilizar esta información para aplicarla al dataset adicional y hacer nuestra predicción, con los nuevos registros, si va a llegar a tiempo o no un envío. Para ver el desempeño de nuestro modelo se nos dio el link a un Dashboard donde comparan nuestra predicción con el resultado "real".

<img src="https://media.istockphoto.com/vectors/scientist-chemist-making-chemical-experiment-vector-id921780612?k=20&m=921780612&s=612x612&w=0&h=5Du0fekt2u_Vq95ooTalcm0uhsnaLKSORoK-hrLIy0E=" height=300>

Esta ultima predicción se encuentra en el archivo [Datathon Jhovany](Jhovanylara.ipynb).

#
Gracias!
![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

