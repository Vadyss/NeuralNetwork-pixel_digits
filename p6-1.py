import math

layer_outputs = [4.8, 1.21, 2.385]
E = math.e

exp_vaules = []

for output in layer_outputs:
    exp_vaules.append(E**output)
    
print(exp_vaules)
    
norm_base = sum(exp_vaules)
norm_values = []

for value in exp_vaules:
    norm_values.append(value / norm_base)

print(norm_values)
print(sum(norm_values))