# Actividad zoo

Vamos a elaborar un programa que nos permita almacenar los animales de un zoo. En concreto nos vamos a centrar en aves, y en particular, en pingüinos y loros. De esta forma, un zoo tiene una lista de animales.

Para ello debemos crear las siguientes clases:

- Una clase Zoo que tenga un nombre que representa el zoo
- Una clase Animal con los atributos nombre, edad y color
- Una clase Loro que hereda de Animal y con un atributo adicional comida
- Una clase Pinguino que hereda de Animal y con un atributo adicional zona que representa la zona donde vive

La clase Zoo debe contener un atributo para almacenar los animales. Debe incluir un método para añadir animales y otro para borrar. También debe incluir un método que describa todos los animales del zoo. Además debe incluir un método para calcular la media y el máximo de edad de los animales. Por último, debe incluir un método que muestre para cada uno de los animales si puede volar. La información del zoo se puede guardar en un fichero de texto, correspondiendo una línea para cada animal.

Crea el código para poder probar todos los métodos propuestos.

## Ejemplo de salida del programa propuesto

```
Animales del zoo: Zoo de Alicante
Pepe fruta
Juan fruta
Andres fruta
Luis Sudáfrica
Alfredo Antártida
#############
Test de vuelo
El loro Pepe puede volar
El loro Juan puede volar
El loro Andres puede volar
El pingüino Luis no puede volar
El pingüino Alfredo no puede volar
#############
Edad media de los animales del zoo:8.6
Edad maxima de los animales del zoo:14
```
