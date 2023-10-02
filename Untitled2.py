#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dado una lista de [FIGUEROA, GARCIA, GUTIERREZ, ISLA, LOPEZ, LUQUE, MAMANI, MARCANI, MONDRAGON, MORENO, MUÑOZ, NAVARRO, OTAZU, PASCACIO, RAMON, TENORIO, VEGAS
]


# In[1]:


lista=('FIGUEROA', 'GARCIA', 'GUTIERREZ', 'ISLA', 'LOPEZ', 'LUQUE', 'MAMANI', 'MARCANI', 'MONDRAGON', 'MORENO', 'MUÑOZ', 'NAVARRO', 'OTAZU', 'PASCACIO', 'RAMON', 'TENORIO', 'VEGAS')
lista


# In[9]:


apellido=input("ingrese el apellido del esstudiante")


# In[10]:


if apellido in lista:
    print(f"El apellido {apellido} pertenece a la lista.")
else:
    print(f"El apellido {apellido} no pertenece a la lista.")


# In[ ]:




