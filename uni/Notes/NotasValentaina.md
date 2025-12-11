# Notas para Valentaina

## Ejercicio 1 

Datos del ejercicio
$na =15$    $x_{A}=8500$   $s_{A}=320$
$nb =12$    $x_{B}=8200$   $s_{B}=280$

### Inciso A 

En el ejercicio te dice de que el intervalo de confianza es eso de 95%, asi que comenzemos por ahi, lo tipico de toda la vida para sacar alpha medios
$$
\begin{aligned}
\text{IC} &= 0.95 \\\\
\alpha &= 0.05 \\\\
\alpha_{/2} &= 0.025
\end{aligned}
$$

Ahora, esta parte es medio que imporante, voy a usar la siguiente formula

$$
   S = \frac{(n_{A}-1)s_{A}^{2}+ (n_{B}-1)s_{B}^{2}}{n_{B}+n_{B}-2}
$$

Una vez que metes los datos consigues q la Desviacion Estandar es 303.05 h 

Ahora, el porque de esta formula especificamente, (hay demasiadas, es por que te menciona varianzas iguales) y el temaño de n no es mayor a 30, es decir es pequeño

despues, sigues con todo el desarrollo, nada fuera de lo normal, sacas grados de libertad:
$$
df= n_{A}+n_{B}-2 
$$
$$ df = 25 $$

sacas el valor critico, es decir t, *INV.T* en el excel, pones la probabilidad y los grados de libertad que acabas de sacar

$$
 t_{0.025,25}=2.0595
$$

Y con eso ya tienes basicamente toda la informacion que necesitas, y como te esta pidiendo un intervalo de confianza la formula es esta

$$
IC = (x_{A}-x_{B})± t_{\alpha/2}*S*\sqrt{\frac{1}{n_{A}}+\frac{1}{n_{B}}}
$$

y ya tienes todos los datos

$$
300 ± 241.73
$$


### Inciso b 

ahora, lo de las hipotesis es bien interesante, ya funciona siempre con la Hipotesis Nula y Hipotesis Alternativa
$$
H_{0} = Hipotesis Nula
$$
$$
H_{A} = Hipotesis Alternativa
$$

y la forma en la que la tienes que pensar es formular la condicion que te piden en el inciso en la alternativa y lo opuesto en la nula, es decir

$$
H_{0} = \mu_{A}-\mu_{B}=0
$$
$$
H_{A} = \mu_{A}-\mu_{B}!=0 \text{     diferencia significativa}
$$

te dice en el ejercicio que
$$
\alpha = 0.05
$$
asi que mantienes ese valor, y ahora tienes que sacar 2 t, una es la t critica, la otra t normal, la t critica la sacas con la formula, de esa no te hagas lio, pero para la otra tienes que seguir la formula acorde al ejercicio, en este caso es:

$$
t= \frac{ (x_{A}-x_{B})-D_{0}}{\sqrt{\frac{s_{A}^2}{n_{A}} + \frac{s_{B}^2}{n_{B}}}}

$$
Ahora, eso de $D_{0}$ es solo para la parte de diferencia de las mu es decir
$$
 D_{0}=\mu_{A}-\mu_{B}
$$

Pero estamos jugando con las reglas de la Hipotesis Nula asi que eso va a ser 0

De ahi sacamos que t es igual a 2.595

Y para la ultima parte, la parte de sacar los grados de libertad de vuelta, pero estos son diferentes, esta vez la formula es:





