import math 

 

x1=int(input ("точне число sqrt(x1): "))  

x2= (int(input("точне число x2 дільник:" ))/int(input("точне число x2 ділене: ")))  

x1_1 = float(input ("наближене число x1: "))  

x2_2 = float(input ("наближене число x2: "))  

 

 

def f (x1, x1_1, x2, x2_2): 

 

    dx1 = abs((math.sqrt(x1) - x1_1)/ math.sqrt (x1)) 

 

    dx2 = abs((x2 - x2_2)/x2) 

 

    if (dx1>dx2): 

 

        print ("Друга рівність точніше",dx2,"<",dx1) 

 

    else: 

 

        print("Перша рівність точніше",dx1,"<",dx2) 

 

f(x1,x1_1,x2,x2_2) 
