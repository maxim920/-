import  math 

def F(x): 

    return 9*x**4 + 12*x**3 - 36*x**2 - 2 

  

  

  

def F1(x): 

    res= 36*x**3 + 36*x**2 - 72*x 

    print(res) 

    return res 

  

  

  

def Method(a, b): 

    try: 

        x0 = (a + b) / 2 

        xn = F(x0) 

        xn1 = xn - F(xn) / F1(xn) 

        while abs(xn1 - xn) > 0.0001: 

            xn = xn1   

            xn1 = xn - F(xn) / F1(xn) 

        print(xn1) 

        return xn1 

    except ValueError: 

        print("Значення не є недійсним: ") 

if __name__ == '__main__': 

   

    a=float(input("A: ")) 

    b=float(input("B: ")) 

    F(x) 

    F1(x) 

     

    print(f'Корінь знаходиться в точці x =', Method(a, b)) 
