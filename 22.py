import re
import os

#[x.group() for x in re.finditer( r'all (.*?) are', 
# 'all cats are smarter than dogs, all dogs are dumber than cats')]

#no match
#matchObj = re.search("^(?!OK|\\.).*", item)



directorio = f"{os.path.dirname(__file__)}\\"
#texto = open(f"{directorio}archivo.txt", "r")




#leido = texto.read()
#primero = re.findall(r'Aliquam (.*?) \\. ', leido)
#print(primero)



 
archivo =  open(f"{directorio}archivo.txt",'r') 
for lineas in archivo:

    lineasfin = str(lineas)
    lineasfin.strip()
    # finding all valid emails
    mails = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}',lineasfin)
    if mails 
        
        
#printing all the valid emails found
print(mails)