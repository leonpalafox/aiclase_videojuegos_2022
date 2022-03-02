import numpy as np

def opt_fun(*arg, fun_num):
  X = arg[0]
  Y= arg[1]
  if len(arg)>2:
    Z = arg[2]
  if fun_num == 0:
    return (X**2 - 10 * np.cos(2 * np.pi * X)) + (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20
  if fun_num == 1:
      a = 20
      b = 0.2
      c = 2 * np.pi
      sum_sq_term = -a * np.exp(-b * np.sqrt(X*X + Y*Y) / 2)
      cos_term = -np.exp((np.cos(c*X) + np.cos(c*Y)) / 2)
      return a + np.exp(1) + sum_sq_term + cos_term
  if fun_num == 2:
     return X**2 + Y**2 + Z**2
  if fun_num == 3:
     return -np.cos(X)*np.cos(Y)*np.exp(-((X-np.pi)**2+(Y-np.pi)**2))
  if fun_num == 4:
      return np.sin(X+Y)+(X-Y)**2-1.5*X+2.5*Y+1
  if fun_num == 5:
    return (X**2 - 10 * np.cos(2 * np.pi * X)) + (Y**2 - 10 * np.cos(2 * np.pi * Y)) + (Z**2 - 10 * np.cos(2 * np.pi * Z)) + 20