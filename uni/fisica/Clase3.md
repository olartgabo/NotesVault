---
id: Clase3
aliases: []
tags: []
---

Digamos que tenemos la siguiente ecuacion vdd, y lo que tengo es que ahora tomo tanto $E$ como $d$ como diferenciales

$\vec{E}= K_e \frac{q}{r^2} \vec{r}$

$\vec{dE}= K_e \frac{dq}{r^2} \vec{r}$

y lo que hago es despejar para E 


$$
\vec{E} = k\int \frac{dq}{r^2} \vec{r}
$$

y cuando no estamos hablando de vectores la formula es algo asi 

$$
E = k\int \frac{dq}{r^2} 
$$


$$
\lambda= \frac{Q}{L}
$$
donde $\lambda$ es igual a la densidad de carga lineal

donde podemos igual aplicar diferencial y despejar
$$
\lambda= \frac{dq}{dl}
$$
$$
dq= \lambda dl
$$
y entonces nuestra formula de e es :

$$
E = k\int \frac{\lambda dl}{r^2} 
$$

tambien tenemos

$$
\sigma = \frac{Q}{A}
$$

donde $\sigma$ es igual a la densidad de carga superficial
donde vamos a hacer exactamente lo mismo
$$
\sigma = \frac{dq}{da}
$$
$$
dq=\sigma da
$$

$$
E = k\int \frac{\sigma da}{r^2} 
$$


$$
\rho  = \frac{Q}{V}
$$

Donde $\rho$ es igual a la densidad de carga volumetrica
$$
\rho = \frac{dq}{dv}
$$
$$
dq=\rho dv
$$


y como estamos teniendo $dv$ como volumen significa que es igual a $dx dy dz$
$$
E = k\int \frac{\rho dv}{r^2} 
$$

## Ejercicios

### Ejercicio

UNa varilla de 14.0 cm de largo tiene una carga uniforme y su carga total es de -2.uC Determine la magintud y direccion del campo eletrico a lo largo del eje de la varilla en un punto a 36.0 de su centro

L = 14 cm = 0.14m
Q = uC = -tenemos*10^-6C 


usando la formula de hace rato, usamos lambda como tnemeos l 
$$
E = k\int \frac{\lambda dl}{r^2} 
$$
ojo a tomar en cuenta que igual tengo lambda

$$
\lambda = \frac{Q}{L}
$$
asi que la intergral se veria algo asi 

$$
E = k \lambda \int \frac{dl}{r^2} 
$$

y ahora tomando x = l, y definiedno la integral, x=r  

$$
E = k \lambda \int_a^{L+a} {x^-2} dx
$$

y eso se vuelve algo como 

$$
E = k \lambda \frac{x^{-1}}{-1} \Big|_a^{L+a}
$$

y eso es algo como 

$$
E = -k \lambda (\frac{1}{L+A}-\frac{1}{a})


$$

ya tenemos el valor de lambda asi que se puede reemplazar y depues de desarrolar la funcion tenemos

$$
E=\frac{K*Q}{a(L+a)}
$$

