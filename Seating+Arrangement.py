
# coding: utf-8

# In[1]:

# Assuming n=30


# In[2]:

n=30
math=n/3
chem=n/3
physics=n/3
chairs=n/2 #there are 2 rows


# In[3]:

i=0
j=0
print("Row 1\n")
while(i<5):
    print("Math"+"\n"+"Physics"+"\n"+"Chemistry")
    i+=1
print("\nRow 2\n")
while(j<5):
    print("Chemistry"+'\n'+"Physics"+"\n"+"Math")
    j+=1

