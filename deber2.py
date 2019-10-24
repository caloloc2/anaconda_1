# importa las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np

def realizar_muestra(a, b, n=10):
    # devuelve un valor aleatorio dentro de los rangos dados
    return np.random.rand(n)*(b - a) + a

def hit_and_miss(a, b, c, n):
    # obtiene puntos dentro de la grafica de cada funcion y determina si se encuentra bajo o arriba de la grafica
    # si esta bajo la grafica es la parte del area a calcular
    x_dentro, x_fuera = [], []
    y_dentro, y_fuera = [], []
    
    for i in range(n):
        x_r = realizar_muestra(a, b, 1)  # generamos un solo valor 
        y_r = realizar_muestra(0, c, 1)  # generamos un solo valor

        evalf1 = f1(x_r)
        evalf2 = f2(x_r)
        
        if ((y_r < evalf1) and (y_r < evalf2)):  # punto abajo o dentro del area
            if (x_r<0):
                x_dentro += [x_r]  # agrega el punto a la lista
                y_dentro += [y_r]  # agrega el punto a la lista
            else:  # punto fuera de la grafica
                x_fuera += [x_r]  # agrega el punto a la lista
                y_fuera += [y_r]  # agrega el punto a la lista
        else:  # punto fuera de la grafica
            x_fuera += [x_r]  # agrega el punto a la lista
            y_fuera += [y_r]  # agrega el punto a la lista
        
    return x_dentro, y_dentro, x_fuera, y_fuera  # devuelve un arreglo con 4 elementos

def f1(x):
    return x**2;  # evaluamos fx

def f2(x):
    return x+4;  # evaluamos fx

x = np.linspace(-3, 3, 100)  # Rango para la variable x
f1x = f1(x)  # Evaluamos f(x) funcion parabolica
f2x = f2(x)  # Evaluamos f(x) funcion lineal
(a, b, c) = (-3, 3, 8) # puntos para el cuadrado o area general

t_muestras = [10, 100] # aqui puede agregar mas numero de muestras

area_cuadrado = 32 # Esta area siempre conocemos (4x8)

for t in t_muestras:
    puntos = hit_and_miss(a, b, c, t) # obtiene el arreglo de puntos obtenidos aleatoriamente
        
    ## segun los puntos obtenidos, la muestra y el area del cuadrado se calcula el area requerida
    area = float(len(puntos[0]))
    area = float(area / t)    
    area = float(area * area_cuadrado)    
    
    print("Area para n=", t, "es", area)

#grafica las funciones
plt.plot(x, f1x)
plt.plot(x, f2x)
# grafica los puntos bajo y fuera de la curva, mostrando el area a calcular
plt.plot(puntos[0], puntos[1], 'o', color='r')  # Graficamos puntos bajo la curva (tomados para el calculo)
plt.plot(puntos[2], puntos[3], 'o', color='g')  # Graficamos puntos fuera
plt.show()