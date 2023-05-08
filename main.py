import numpy as np
import pandas as pd



def poisson_random_number(mean):
    p = np.exp(-mean)
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
mean_hour= mean_min/60

std = 480.8531584
std_min = std/60
std_hour= std_min/60

for i in range(20):
    print(poisson_random_number(mean_min))

