# input of three integers: 
# N = the number of eyes, 
# T = the number of noses, 
# M = the bumber of mouths

inputList = input().split()
N, T, M = [eval(i) for i in inputList]
# print(type(N), type(T), type(M))
print(N * T * M)
