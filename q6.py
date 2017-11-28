listNames=[]
for counter in range(0,3):
    s=input  ("enter name")
    listNames.append(s)
print (listNames)

listAge=[]
for counter in range(0,3):
    a=input("enter age for "+listNames[counter])
    listAge.append(listNames[counter]+":"+a)
print (listAge)

listMail=[]
for counter in range(0,3):
    c = input("enter mail")
    listMail.append(c)
print (listMail)