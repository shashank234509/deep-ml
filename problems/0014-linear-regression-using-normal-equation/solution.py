import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    x=np.array(X,float)
    y=np.array(y,float)
    
    xt=x.T
    a1=xt@x 
    a2=np.linalg.pinv(a1)
    theta=a2@xt@y
    return np.round(theta, 4).tolist()