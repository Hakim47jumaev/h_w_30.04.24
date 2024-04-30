def number_or_string(a):
    try:
        float(a)
        return True
    except:
        return False
def sum(a,b):
    return int(a)+int(b)   
def min(a,b):
    return int(a)-int(b) 
def div(a,b):
    return int(a)/int(b) 
def mult(a,b):
    return int(a)*int(b) 

a=input()
i=input()
b=input()
if number_or_string(a) and number_or_string(b):
    if i=="+":
        print(sum(a,b))
    if i=="-":
        print(min(a,b))
    if i=="/":
        print(div(a,b))
    if i=="*":
        print(mult(a,b))
else:
    print("error")
