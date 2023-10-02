#!/usr/bin/env python
# coding: utf-8

# # CLASE Y OBJETOS

# In[3]:


class persona:
    nombre=""
    apellido=""
    dni=""
    talla=0


# In[7]:


persona1=persona()
persona1.nombre="brandon"
persona1.apellidoss="isla Cconisllia"
persona.dni="125485"
persona.talla=1.6


print("persona1")
print(f"nombre {persona1.nombre}")
print(f"apellido {persona1.apellido}")
print(f"dni {persona1.dni}")
print(f"talla {persona1.talla}")


# In[24]:


class curso:
    def _init_(self,codigo,nombre,hora,credito):
        self.nombre=nombre
        self.codigo=codigo
        self.hora=hora
        self.credito=credito

   
    


# In[26]:


def motrar_Datos_curso(self):
    print(f"curso {self.nombre}")
    print(f"codigo { self.codigo}")
    print(f"hora {self.hora}")
    print(f"credito {self.credito}")


# In[ ]:


curso1=curso("co501","logica",3,4)


# In[ ]:


curso1.mostrar_Datpss_curso()


# In[ ]:




