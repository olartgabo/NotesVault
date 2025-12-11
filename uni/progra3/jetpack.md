# JetPack Compose

### Padding
Padding termina siendo un tipo de relleno desde elemento hasta border, termina siendo solo para adentro

### Margin
Padding pero para afuera, toda la idea de ampujgar a elementos, dejar espacio entre 

JetPack Compose termina tratandose de usar 

@Composable dentro del MainActivity, para llamar a funcione dentro de la funcion main para poder, mostrar elementos visuales, 
Termina siendo una version mas sobredesarrolada de algo como tailwind, pero misma estructura modular  y de ejecucion para area visual

@Preview, para la parte de mostrar codigo mostrar como se ve, 
@Preview(showBackground = true, showSystemUi = true) es uno de los parametros que se le puede pasar 

ahora, una nota, cuando estoy ejecutando como tal codigo, si va a haber algo que se va a ejecutar es solo el composable, si es de que dice algo de preview, termina siendo solo para la vista dentro del Android Studio, despuse no sirve para absolutamente nada ,mas 


```kotlin
@Preview
@Composable
fun Prueba()
{
    Text(text = "Qtal")
}
```


es un ejemplo de funcion
