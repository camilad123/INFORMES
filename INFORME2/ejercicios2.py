# -*- coding: utf-8 -*-
"""ejercicios2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Za7GZ1koEmYh_HZ0oDYnzshHGGCexvXX

EJERCICIO 1
"""

nombre_completo="Camila Duran Salazar"

#Ejercicio 1

precios = {
    "A001":[31000], 
    "A011":[25000], 
    "A032":[43000],
    "A125":[55000],
    "B001":[10000],
    "B005":[20000],
    "P009":[30000],
    "P019":[49000],
    "R001":[60000],
    "W307":[90000],
    "Z052":[35000],
    "Z025":[27000],
    "Z278":[65000]
}

ventas = [
    "A032-52Unidades","B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades", 
    "B005-20Unidades","B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades",         
    "A011-31Unidades", "P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades",
    "A001-12Unidades", "A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades",
    "Z025-42Unidades", "Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades",
    "A001-31unidades","A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades",
    "P009-19Unidades","B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades",
    "W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades",
    "P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades",
    "W307-31Unidades","Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades",
    "Z278-11Unidades","A001-91unidades"
]


for venta in ventas:
   
    producto, unidades = venta.split("-")
   
    if producto in precios.keys():
        un=[]
        for char in unidades:
            if char.isdigit():
               un.append(char)
        
        precios[producto].append(int("".join(un)))

print(f'Diccionario "precios"\n{precios}\n')

unidadesPorProducto ={k:sum(v[1:]) for k,v in precios.items()}
print(f'Diccionario Unidades por Producto \n{unidadesPorProducto}\n') 

ventasPorProducto={k:sum(v[1:])*v[0] for k,v in precios.items()}
print(f'Diccionario Ventas por Producto \n{ventasPorProducto}\n')

ventasTotal=sum(ventasPorProducto.values())
print(f'Ventas en Total \n{ventasTotal}\n')

reporteVentas = [unidadesPorProducto, ventasPorProducto, ventasTotal]
print(f'Reporte de ventas \n{reporteVentas}\n')

"""EJERCICIO 2"""

#Ejercicio 2

import pandas as pd
import numpy as np


calificaciones = {
                      "Cristian Pachon":       {"Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.2,   "Artes": 4.0,  "Musica": 0.5},
                      "Daniela Pineda":        {"Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 4.0,   "Artes": 3.1,  "Musica": 4.0},
                      "Esteban Murcia":        {"Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 3.1,   "Artes": 0.0,  "Musica": 3.1},
                      "Jose Guzman":           {"Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.2,  "Musica": 0.0},
                      "Camilo Rodriguez":      {"Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 1.0,  "Musica": 0.2},
                      "Mariana Londoño":       {"Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.3,  "Musica": 1.0},
                      "Estefania Muños":       {"Fisica":  5.0,   "Ingles": 1.2,   "Deportes": 1.2,   "Artes": 1.9,  "Musica": 1.3},
                      "Cristian Rodriguez":    {"Fisica":  0.2,   "Ingles": 2.9,   "Deportes": 1.0,   "Artes": 4.2,  "Musica": 1.9},
                      "Natalia Alzate":        {"Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                      "Juan Sanabria":         {"Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                      "Juanita Calderon":      {"Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 0.5,  "Musica": 4.2},
                      "Laura Quintero":        {"Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 4.2,   "Artes": 0.0,  "Musica": 0.5},
                      "Viviana Quesada":       {"Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 2.3,   "Artes": 4.2,  "Musica": 0.0},
                      "Camila Alzate":         {"Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 2.5,   "Artes": 4.3,  "Musica": 3.2},
                      "Leonidas Sanabria":     {"Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 4.2,   "Artes": 2.5,  "Musica": 4.3},
                      "Juana Diaz":            {"Fisica":  4.1,   "Ingles": 0.0,   "Deportes": 4.5,   "Artes": 4.2,  "Musica": 2.5},
                      "Laura Playonero":       {"Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 0.5,   "Artes": 4.5,  "Musica": 3.2},
                      "Viviana Restrepo":      {"Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                      "Elias Rodriguez":       {"Fisica":  2.2,   "Ingles": 0.5,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                      "Mariana Pacheco":       {"Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                      "Estefany Muñoz":        {"Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 3.1,   "Artes": 4.0,  "Musica": 4.0},
                      "Cristian Fernandez":    {"Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 0.0,   "Artes": 3.1,  "Musica": 3.1},
                      "Jessika Arias":         {"Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.0,  "Musica": 0.2},
                      "Juan Mendoza":          {"Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                      "Maria Calderon":        {"Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 1.0},
                      "Laura Lozada":          {"Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.0,  "Musica": 1.3},
                      "Yessica Quesada":       {"Fisica":  1.2,   "Ingles": 5.0,   "Deportes": 1.9,   "Artes": 1.2,  "Musica": 1.3},
                      "Jennifer Alzate":       {"Fisica":  2.9,   "Ingles": 0.2,   "Deportes": 4.2,   "Artes": 1.0,  "Musica": 1.9},
                      "Karen Sanabria":        {"Fisica":  0.0,   "Ingles": 4.1,   "Deportes": 4.2,   "Artes": 4.5,  "Musica": 2.5},
                      "Fernando Rodriguez":    {"Fisica":  0.5,   "Ingles": 2.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                      "Nina Londoño":          {"Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 2.5,   "Artes": 4.2,  "Musica": 4.3},
                      "Favio Munera":          {"Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                      "Lindsey Roy":           {"Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                      "Nathalia Hernandez":    {"Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 0.0,   "Artes": 4.2,  "Musica": 0.5},
                      "Juan Gaviria":          {"Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 4.2,   "Artes": 2.3,  "Musica": 0.0},
                      "Fabio Urrego":          {"Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 4.3,   "Artes": 2.5,  "Musica": 3.2},
                      "Fernanda Quintero":     {"Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                      "Camila Queiroz":        {"Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 4.5,   "Artes": 0.5,  "Musica": 3.2},
                      "Ursula Alzate":         {"Fisica":  2.2,   "Ingles": 4.0,   "Deportes": 4.2,   "Artes": 0.5,  "Musica": 2.0},
                      "Aureliano Buendia":     {"Fisica":  1.0,   "Ingles": 3.1,   "Deportes": 4.0,   "Artes": 4.0,  "Musica": 2.2},
                }

df = pd.DataFrame(data=calificaciones) #Dataframe a partir del diccionario, prodremos ver de manera ordenada los datos del mismo. 
df.round(2) # Mostramos el dataframe generado

df2 = df.mean(axis=0)
df3 = df2.to_dict()
df3
K = 2

promediosPorEstudiante = dict() 
for key in df3: 
      
    
    promediosPorEstudiante[key] = round(df3[key], K) 
promediosPorEstudiante

df4 = df.mean(axis=1) 
df5 = df4.to_dict() 

K = 2

promediosPorMateria = dict() 
for key in df5: 
      
    
     promediosPorMateria[key] = round(df5[key], K) 
promediosPorMateria

## Estudiantes que aprueban:
est = df2
est = est[df2 > 3 ]
est.to_dict()
estudiantesAprobados = list(est.keys())
estudiantesAprobados

## Estudiantes que repueban: 
est2 = df2
est = est[df2 < 3]
est.to_dict()
estudiantesReprobados = list(est2.keys())
estudiantesReprobados

reporteEstudiantes = [promediosPorEstudiante, promediosPorMateria, estudiantesAprobados, estudiantesReprobados]
reporteEstudiantes

"""EJERCICIO 3"""

# precioEntradas={
#     'lunes-viernes':{
#         '2D':{'NIÑOS':5000,'ADULTOS':8000},
#         '3D':{'NIÑOS':8000,'ADULTOS':12000}
#     },
#     'sabado-domingo':{
#         '2D':{'NIÑOS':7000,'ADULTOS':9000},
#         '3D':{'NIÑOS':9000,'ADULTOS':15000}
#     }
# }

preciosEntradas={
    '2D':{'NIÑOS':(5000,7000),'ADULTOS':(8000,9000)},
    '3D':{'NIÑOS':(8000,9000),'ADULTOS':(12000,15000)}
}

ventas=[
   ("2D_3NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_1ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_3ADULTOS_LUNES"),("3D_3NIÑOS_LUNES", "3D_4ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_4ADULTOS_LUNES"),("2D_1NIÑOS_MARTES",
    "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),
   ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),(
    "2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),
   ("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"), ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),(
    "2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES",
    "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
    "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),(
    "2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
    "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES",
    "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_2NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES",
    "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),(
    "3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),
   ("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),(
    "2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),
   ("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO",
    "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_DOMINGO", "2D_0ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"), ("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO",
    "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO",
    "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO","2D_4ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_9ADULTOS_DOMINGO")
]


tipos_cine=[]
cantidad_boletos=[]
tipo_boleto=[]
dia_semana=[]

for tup in ventas:
    for e in tup:
        tipo_cine, boleto, dia = e.split('_')
        un,tipo=[],[]
        for char in boleto:
            if char.isdigit():
                un.append(char)
            else:
                tipo.append(char)

        tipos_cine.append(tipo_cine)
        cantidad_boletos.append(int(''.join(un)))
        tipo_boleto.append(''.join(tipo))
        dia_semana.append(dia)

print(f'Lista tipos_cine\n{tipos_cine}\n')
print(f'Lista cantidad_boletos\n{cantidad_boletos}\n')
print(f'Lista tipo_boleto\n{tipo_boleto}\n')
print(f'Lista dia_semana\n{dia_semana}\n')

boletasVendidas = sum(cantidad_boletos)
print(f'Boletas vendidas: {boletasVendidas}')

dineroRecaudado=[]

for cantidad, cine, edad, dia in zip(cantidad_boletos, tipos_cine, tipo_boleto, dia_semana):

    if dia in 'SABADO' or 'DOMINGO':
        recaudo=cantidad*preciosEntradas[cine][edad][1]
        dineroRecaudado.append(recaudo)
    else:
        recaudo=cantidad*preciosEntradas[cine][edad][0]
        dineroRecaudado.append(recaudo)

dineroRecaudado=sum(dineroRecaudado)
print(f'Dinero recaudado: {dineroRecaudado}')

"""EJERCICIO 4"""

#Ejercicio 4
# #obtenerMultiplos: Función para generar los primeros 10 multiplos de un numero.

def obtenerMultiplos(numero):

  return [numero * i for i in range(1, 10 + 1)]

obtenerMultiplos(20)

#obtenerDivisores: función para generar una lista de todos los divisores positivos de un número.

def obtenerDivisores(numero):
    """
    Genera una lista de los divisores de un número.
    """
    lista = [i for i in range(1, numero + 1) if numero % i == 0] 
    lista.pop(0)
    a = len(lista)
    lista.pop(a-1)
    
    return lista

obtenerDivisores(1000)

from numpy.lib.function_base import bartlett
#Secuencia de Fibonacci - Recursiva:

def obtenerNesimoFibonacci(num):
  if  num==0:
    return 0
  elif num ==1:
    return 1
  else:
    return obtenerNesimoFibonacci(num-1) + obtenerNesimoFibonacci(num-2)
 

obtenerNesimoFibonacci(25)

funciones = [ obtenerMultiplos, obtenerDivisores, obtenerNesimoFibonacci]

"""EJERCICIO 5"""

#Ejercicio 5


def calcularSalario(Nombre, cantidadArticulos):
  
    cantidadArticulos = (1380000 + cantidadArticulos[0] * 5000 + cantidadArticulos[1] * 2800 + cantidadArticulos[2] * 2400 + cantidadArticulos[3] * 1750 + cantidadArticulos[4] * 1750 + cantidadArticulos[5] * 2400 + cantidadArticulos[6] * 1900)
    return {"nombre": Nombre, "salario": cantidadArticulos}

calcularSalario("Juan",[3,1,2,1,1,1,1])