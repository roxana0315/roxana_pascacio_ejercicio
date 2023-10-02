#!/usr/bin/env python
# coding: utf-8

# In[4]:


def saludo():
    print("bienvenido al curo lp3")
    print("*****puthon*****")


# In[5]:


saludo()


# In[13]:


def factorial(numero):
    fac=1
    for i in range(1,numero+1):
        fac*=i
    print(f"el factorial de {fac}")


# In[14]:


numero=int(input("ingree numero"))
factorial(numero)


# In[15]:


def saludo2():
    mensaje="bienvenid lp3"
    return mensaje


# In[19]:


saludo2


# In[21]:


def obtenerigv(importe):
    return importe*0.19


# In[23]:


obtenerigv(150)


# In[ ]:




