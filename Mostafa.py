#!/usr/bin/env python
# coding: utf-8

# In[1]:


##taske one exaple one for Mostafa Khaled Sayed Ali
value=15;
print("the value is :",value)
print(f'the same value is{value}')
b=value==5
print(b)
anser_1=15
anser_2="Hello"
print(f'the type is:{type(anser_1)}')
print(f'the type is:{type(anser_2)}')
v1=12.3
v4=[1,2,3]
v2="123"
v3={1,2,3}
print(f"the type is variable is:{v1}")
print(f"the type is variable is:{v2}")
print(f"the type is variable is:{v3}")
print(f"the type is variable is:{v4}")


# In[2]:


## taske one section tow for Mostafa Khaled
val1="Ault"
val2="kelly"
print(val1+val2)
print(val1,val2)
print(f"{val1}{val2}")
valtotal=val1+val1
x=''.join(reversed(valtotal))

print(valtotal[::-1])
print(x)

print(x[0]=='r')
print(x[0]=='t')
text="hello World"
print(text[0])
print(text[2:5])
print(text.upper())
print(text.lower())


# In[ ]:


list1=[100,200,300,400,500]
l=list1.reverse()
frits=["apple","banana","cherry"]
print(frits[1])
frits[0]='kiwi'
print(frits)
frits.insert(1,'lemone')
print(frits)
print(frits[-1])
frits=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(frits[3:6])
list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
sub_list=['h','i','j']
list1[2][1][2][2:]=sub_list
print(list1)

