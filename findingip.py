from random import randint

def dbip():
    return randint(0,9)

ip=dbip() 
print(ip)

f=open("ip_generated.txt","w")
f.write(str(ip))
