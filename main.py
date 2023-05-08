import numpy as np
import pandas as pd
import math


def poisson_random_number(mean):
    p = np.exp(-1/mean)
    pp = p
    i = 0
    R = np.random.uniform(0,1)
    while R > pp:
        R = R * np.random.uniform(0,1)
        i +=1
    return i



time_limit = 60 * 60 * 24 * 10
t =0

mean = 395.423341
mean_min = mean/60
print("mean_min = ",mean_min)

mean_hour= mean_min/60

std = 480.8531584
std_min = std/60
std_hour= std_min/60

for i in range(20):
    poisson = poisson_random_number(mean_min)
    print("poisson : ",poisson)
    f = lambda x :  ((mean_min**x)/(math.factorial(x)))*np.exp(-1/mean_min) 
    rand = f(poisson)
    print(rand)