#!/usr/bin/env python
# coding: utf-8

# In[2]:


firstname = str(input("first name is: "))
lastname = str(input("last name is: "))
result = lastname+" "+firstname
print("the full name is:")
print(result)


# In[13]:


number = int(input("the number is: "))
result = number + (number * 11) + (number * 111)
print("your result is:")
print(result)


# In[1]:


num = int(input("the number is: "))  
if (num % 2) == 0:  
print("{0} is even number".format(num))  
else:  
print("{0} is odd number".format(num))  


# In[3]:


nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))


# In[7]:


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
x=int(input())
print(fact(x))


# In[8]:


def odd_values_string(str):
result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
    result = result + str[i]
      return result
print(odd_values_string('gomycode'))


# In[21]:


def getDiscount(amount):
    if amount < 200:
        return amount*0.1;
    elif amount >= 200:
        return amount*0.3;
    elif amount >= 500:
        return amount*0.5;
    else:
        return amount*1;

if __name__=='__main__':
    selling_price = int(input("Enter selling price : "))
    discount = getDiscount(selling_price)

    print("Discount: {}".format(discount))

