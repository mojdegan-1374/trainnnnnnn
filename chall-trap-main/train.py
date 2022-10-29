#t1
a = input("username: ")
b = input ("password: ")

def hello(a, b):
    user = "milad"
    passs = "milad"
    
    if user == a and passs == b:
        print("doroste")
    else:
        print("ghalate")
        
hello(a, b)
print ("hello")


#t2

e = input("adad aval: ")
f = input("adad dovom: ")

def chax(e , f):
    sum = int(e) + int(f)
    g = sum
    print(g)
    if sum % 2 == 0:
        print("zoj")
    else:
        print("fard")
chax(e , f)            
