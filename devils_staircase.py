"""
Script to print 'devils staircase' of the cantor set.
"""
import numpy as np
import matplotlib.pyplot as plt



def d(n,x):
    """
    compute the terms of the devils staircase function:
    
            dn(3x)/2         , 0 <= x <= 1/3
    dn+1 =  1/2              , 1/3 <= x <= 2/3
            1/2 + dn(3x-2)/2 , 2/3 <= x <= 1

    n: number of iteration steps
    x: argument of the function 
    """
    if(n == 0):
        return x
    elif(0 <= x <= 1/3):
        return d(n - 1,3*x)/2
    elif(1/3 < x <= 2/3):
        return 1/2
    elif(2/3 < x <= 1):
        return 1/2 + d(n - 1,3*x - 2)/2
        
        


def main():
    """
    computes the devils staircase function and plots it linearly and 
    double logarithmic.
    """
    n = 100
    
    X = np.linspace(0,1,101)
    Y = [d(n,x) for x in X]
    
    plt.figure(1)
    plt.plot(X,Y)
    
    plt.figure(2)
    plt.loglog(X,Y)
    
    plt.show()

if __name__=="__main__":
    main()