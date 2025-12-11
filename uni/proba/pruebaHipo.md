# Prueba de hipotesis para diferencia de proporciones


Formulas basicas:

$$
p_{1}=\frac{x_{1}}{n_{1}}
$$

$$
p_{2}=\frac{x_{2}}{n_{2}}
$$

donde x es el numero de exitos y n es la muestra 


ademas, se tiene

$$

P=\frac{x_{1}+x_{2}}{n_{1}+n_{2}}
$$

Estadistico de Prueba

$$

z=\frac{p_{1}-p_{2}}{\sqrt{p(1-p)(\frac{1}{n_{1}}+\frac{1}{n_{2}})}}

$$


En una ciudad turistica, un hotel quiere decidir si convierte sus habitaciones en instalaciones de no fumadores
En una muestra de 400 huespedes el año anterior 166 personas solicitaron habitaciones para no fumadores
Este año 175 huespedes de 380 si solicitaron habitaciones para fumar 
Con un nivel de significancia del 1%  
Mediante prueba de hipotesis que recomiendas como decision al hotel?



## Prueba de hipotesis para varianzas

$$
H_{0}: \sigma_{1}^2 = \sigma_{2}^2
$$
$$
H_{A}:  \sigma_{1}^2 < \sigma_{2}^2          ,        \sigma_{1}^2 > \sigma_{2}^2           ,    \sigma_{1}^2 != \sigma_{2}^2  
$$
$$
NC = 1- \alpha
$$

Estadistico de prueba es 

$$
F=\frac{s_{1}^2}{s_{2}^2}
$$


Ejemplo:
En un proceso se quiere comparar la variabilidad con el peso en 2 lineas de produccion con los siguientes datos 
Linea A 
n = 15
promedio = 10.5 
s1 = 2.42

Linea B 
n = 12
promedio = 11.2  
s1 = 2.32

## Prueba de independencia de Atributos 
Comparacion entre variables atributos que presentan valores de frecuencia y se quiere comparar su independencia 

$$
x^2 = \frac{\sum (o_{i}-e_{i})^2}{e_i}
$$

donde
$o_{i}$ es el valor observado
$e_{i}$ es el valor esperado


Ejemplo
En pruebas con nuevas vacunas para la gripe estacional se obtuvo los siguientes


$$
H_{0}:\text{Los atributos son independientes}
$$
$$
H_{A}:\text{Existe alguna dependencia o relacion entre atributos}
$$

$$
gl:V=(f-1)*(c-1)
$$

En este caso grados de libertad es 2 
se usa entonces *INVCHICUAD* (Area, gl) - $(0.95;2)$ = 5.99
entonces valor critico 5.99 y de ahi para la derecha , con lo que teniamos de la formula ei, damos por conclusion que $H_{0}$ queda rechazado``
