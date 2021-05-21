import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    n = np.size(x)

    mean_x, mean_y = np.mean(x), np.mean(y)
    
    #Implementation of minimun square method
    summatory_xy = np.sum((x-mean_x)*(y-mean_y))
    summatory_xx = np.sum(x*(x-mean_x))

    #Coefficients
    b1 = summatory_xy/summatory_xx
    b0 = mean_y - b1*mean_x

    return(b0,b1)
    
#Graph function
def plot_regression(x,y,b):
    plt.scatter(x, y, color = 'g', marker= 'o', s = 30)
    
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = 'b')

    #Labels
    plt.xlabel('x - Independent')
    plt.ylabel('y - Dependent')

    plt.show()

#Main function (Testing values)
def main():
    #Dataset
    x = np.array([1,2,3,4,5])
    y = np.array([2,3,5,6,5])

    #Getting estimation coefficients
    b = estimate_coef(x,y)
    print('b0 = {}. b1 = {}'.format(b[0],b[1]))

    plot_regression(x,y,b)

if __name__ == '__main__':
    main()