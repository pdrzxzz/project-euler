a = 1
b = 1
c = a+b
sum_of_evens = 0
while c < 4*(10**6):
    sum_of_evens += c
    a = b + c
    b = a + c
    c = a + b

print(sum_of_evens)