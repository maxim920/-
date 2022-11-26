import numpy as np 

a = np.matrix('4 1 4; 1 1 2; 2 1 2') 

b = np.matrix('-2; -1; 0') 

print('A=', a) 

print('B=',b) 

a_inv = np.linalg.inv(a) 

print(a_inv) 

x = a_inv.dot(b) 

print('X=',x) 
