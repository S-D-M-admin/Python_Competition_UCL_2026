##ROUND 1: Integer Complexity##

#The Integer Complexity of a Number, given by the function IC(x), is the fewest number of 1s required to form x solely through addition and multiplication:
#IC(11)=8 because 11=(1+1+1)*(1+1+1)+1+1 and has no representation with fewer ones

#Your job is to find IC(x) for as many x as possible. You will create a list and then append that list to a text file in under a minute.
import time
import random
import sympy
import numpy
import itertools
import statistics
import pandas
import bisect
import math
from sympy import factorint

duration_seconds = 60  # 1 minute
output_file = "ICCollated.txt"
ICCollated = [0,1]
x = 2

# Code for IC Integer Complexity function below returns 5.4 million entries to ICCollated in one minute

def IC(x):
    factors = factorint(x)
    return ICCollated[x-1] + 1 if x in factors.keys() else sum([ICCollated[k]*v for k, v in factors.items()])

start_time = time.time()
while time.time() - start_time < duration_seconds:
    ICCollated.append(IC(x))
    x += 1

# Save to a line-separated text file
with open(output_file, "w", encoding="utf-8") as f:
    for item in ICCollated:
        f.write(f"{item}\n")

print(f"Completed. Saved {len(ICCollated)} entries to '{output_file}'.")
