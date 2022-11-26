import math 

  

a = 1.0; b = 2.0; e = 0.0001 

def f(x): 

    return 9*x**4 + 12*x**3 - 36*x**2 - 2 

y1 = f(a); y2 = f(b) 

if y1 * y2 >= 0: 

    print ("Коренів нема") 

else: 

    n = 1 

    x = (a+b)/2 

    y3 = f(x) 

    while (abs(y3) > e): 

        x = (a+b)/2 

        y3 = f(x); 

        print(x) 

        if y1 * y3 < 0: 

            b = x 

             

        else: 

            a = x 

            n += 1 

             

    print ("x = %15.10f" % (x)) 
