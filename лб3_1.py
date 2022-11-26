import  math  

 

def F(x):  

 

    return 9*x**4 + 12*x**3 - 36*x**2 - 2  

 

   

 

   

 

def F1(x):  

 

    res= 36*x**3 + 36*x**2 - 72*x  

 

    print(res)  

 

    return res  

 

a = 1 

 

b = 2 

 

eps = 0.001 #точність 

 

def newton(a,b,eps): 

 

    df2 = derivative(F, b, n = 2) 

 

    if ((b)*df2>0): 

 

        xi = b 

 

    else: 

 

        xi = a 

 

    df = derivative(F1,xi, n= 1) 

 

    xi_1 = xi - F1(xi)/df 

 

    while (abs(xi_1 - xi)>eps): #accuracy check 

 

        xi = xi_1 

 

        xi_1 = xi - F(xi)/df 

 

        return print ('За методом Ньютона x = ', xi_1) 

 

newton (a,b,eps) 
