# Máquina de Galton

## Simulación

* Será la simulación de una máquina de Galton de 3000 canicas. 
* En total tendrá 12 niveles de obstáculos, deberás decidir si va a caer a un lado o al otro 12 veces.
* El resultado final será un histograma que represente la cantidad de canicas en cada contenedor, no olvides colocar nombre a los ejes y un título al gráfico. 
* Deberás emplear dos funciones, una para calcular los resultados de las canicas y la segunda para la graficación del histograma. 

## Explicación paso a paso

* Primeramente coloqué el módulo random de la librería de python, para generar la elección aleatoria de la dirección de la canica.
* Posterior al módulo random coloque la librería Matplotlib especializada en la creación de gráficos de dos dimensiones.
* Teniendo ya las librerías que necesito para mi código, procedo a definir las funciones que ocuparé para la simulación de la máquina de Galton, utilizando la palabra reservada def, seguida del nombre que elegí, paréntesis y dentro de estos los parámetros de entrada, terminando con dos puntos. 
* Cree una lista llamada conteiners con num_levels, todos los elementos inicializados en 0. Esta lista representa los contenedores y su conteo inicial de canicas.
* Inicié un bucle que itera num_marbles, simulando el movimiento de cada canica. Dentro del bucle, la variable position establece la división entera de num_levels entre 2. Esto para establecer que la posición de la canica este en el contenedor central.
* Inicié otro bucle que itera num_levels. Cada iteración representa un nivel de los contenedores. Dentro de este bucle interno, la variable direction con el random.choice se establece de forma aleatoria en -1 o 1, lo que representa si la canica cae hacia la izquierda o hacia la derecha. La posición de la canica se actualiza sumándole el valor de direction. Esto simula el movimiento de la canica dentro de los contenedores.
* Después utilicé el condicional if para saber si la position se vuelve menor que 0, se reinicia a 0, asegurando que la canica se mantenga dentro del rango de contenedores.
* En caso de que no se cumpla el primer condicional coloqué un elif donde se puede establecer que si la position se vuelve mayor o igual a num_levels, se establece en num_levels - 1, asegurando que la canica se mantenga dentro del rango de contenedores, teniendo en cuenta que el índice es cero. Después de que el bucle interno se completa, se incrementa en 1 el valor en conteiners[position], indicando que una canica ha caído en ese contenedor. Una vez que se ha simulado el movimiento de todas las canicas, la instrucción return devuelve la lista conteiners, que representa el conteo final de canicas en cada contenedor.
* Defino la función para la gráfica de galton nuevamente con la palabra reservada def, en donde muestre los resultados de la simulación. Dentro de esta función utilicé el plt.bar para crear una gráfica de barras, la lista conteiners representará la altura de cada barra.
* Para establecer los nombres de los ejes x e y, así como el titulo de la gráfica utilice plt.xlabel, plt.ylabel y plt.title. El plt.show() muestra la gráfica en una ventana emergente.
* Definí dos variables para representar la cantidad de canicas(num_marbles) y el número de niveles(num_levels).
* A continuación, se llama a la función galton_machine con num_marbles y num_levels como argumentos para simular el funcionamiento de la máquina de Galton. Los resultados de la simulación se guardan en la variable results.
* Por último, se llama a la función graphic_Galton pasando results como argumento para mostrar el gráfico de barras con los resultados de la simulación.

## Reflexiones

No cabe duda que ha sido todo un reto el proyecto de esta semana, pero con la ayuda de los materiales que nos proporcionan y la excelente aportación de nuestro profesor para aclarar dudas lo he culminado. Cada día se aprende algo nuevo, solo basta dedicarle el tiempo necesario para el desarrollo de nuevas habilidades en lo que a python se refiere. Reconozco que cada clase que he tenido me ha ayudado para entender mejor los temas dentro de cada módulo, sus aclaraciones me han servido para terminar cada proyecto que he realizado. 