#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dado el precio de 3 productos ingresados por el teclado, aplicar un descuento del 10% si la enta es mayor o igual a 1000


# In[2]:


# Solicitar al usuario que ingrese los precios de los 3 productos
precio_producto1 = float(input("Ingrese el precio del primer producto: "))
precio_producto2 = float(input("Ingrese el precio del segundo producto: "))
precio_producto3 = float(input("Ingrese el precio del tercer producto: "))

# Calcular el precio total
precio_total = precio_producto1 + precio_producto2 + precio_producto3

# Verificar si el precio total es mayor o igual a 1000
if precio_total >= 1000:
    # Aplicar un descuento del 10%
    descuento = 0.10 * precio_total
    precio_total -= descuento
    print(f"El precio total con un 10% de descuento es: ${precio_total:.2f}")
else:
    print(f"El precio total sin descuento es: s/. {precio_total:.2f}")


# In[3]:


# Lista de nombres de estudiantes
conjunto_salon ={'FIGUEROA', 'GARCIA', 'GUTIERREZ', 'ISLA', 'LOPEZ', 'LUQUE', 'MAMANI', 'MARCANI', 'MONDRAGON','MORENO', 'MUÑOZ', 'NAVARRO', 'OTAZU', 'PASCACIO', 'RAMON', 'TENORIO', 'VEGAS'
            }

# Solicitar al usuario que ingrese un nombre
nombre_estudiante = input("nombre del estudiante: ")

# Verificar si el nombre está en la lista
if nombre_estudiante in conjunto_salon:
    print(f"{nombre_estudiante} está en la lista de estudiantes del salón.")
else:
    print(f"{nombre_estudiante} no está en la lista de estudiantes del salón.")


# In[4]:


#dado el importe total de ventas realizadas por un trabajor (ingresado por teclado) categorizar que tipo de empleado es, considerando la 
#siguiente tabla
# categoria: A [0, 1000]
# categoria: B [1000, 2000]
# categoria: C [2000, 5000]
# categoria: D [5000, mas]


# In[5]:


# Solicitar al usuario que ingrese el importe total de ventas
importe_ventas = float(input("Ingrese el importe total de ventas: "))

# Categorizar al empleado
if importe_ventas <= 1000:
    categoria = "A"
elif 1000 < importe_ventas <= 2000:
    categoria = "B"
elif 2000 < importe_ventas <= 5000:
    categoria = "C"
else:
    categoria = "D"

# Imprimir la categoría del empleado
print(f"El empleado pertenece a la categoría {categoria}")


# In[7]:


# Solicitar al usuario que ingrese el importe total de ventas
importe_ventas = float(input("Ingrese el importe total de ventas: "))

# Categorizar al empleado
if importe_ventas <= 1000:
    categoria = "A"
else:
    if importe_ventas <= 2000:
        categoria = "B"
    else:
        if importe_ventas <= 5000:
            categoria = "C"
        else:
            categoria = "D"

# Imprimir la categoría del empleado
print(f"El empleado pertenece a la categoría {categoria}")


# In[ ]:





# In[8]:


# Solicitar al usuario que ingrese el importe total de ventas
importe_ventas = float(input("Ingrese el importe total de ventas: "))

# Categorizar al empleado
if importe_ventas <= 1000:
    categoria = "A"
elif 1000 < importe_ventas <= 2000:
    categoria = "B"
elif 2000 < importe_ventas <= 5000:
    categoria = "C"
else:
    categoria = "D"

# Imprimir la categoría del empleado
print(f"El empleado pertenece a la categoría {categoria}")


# In[9]:


range(5)


# In[10]:


for numero in range(11):
    print (numero)


# In[11]:


for numero in range(10, 22, 2):
    print (numero)


# In[12]:


numero = 1
fin = 10 
while numero <= fin:
    print(numero)
    numero+=1


# In[ ]:




