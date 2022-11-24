# QALY = the product of Ql (0 or 1) and length of period

# N = number of periods of constant quality during a persons lifetime
# following N lines = two real numbers, first between 0 and 1 rep. quality of life in the period, second between 0 and 100 rep. years in this period 

N = int(input())

# returns the value as list of strings 
qaly_period = [input().split() for i in range(N)] 
# returns list with the product of each pair of values
product_qaly_period = [float(x) * float(y) for x,y in qaly_period]

qaly_lifetime = sum(product_qaly_period)

print(qaly_lifetime)

