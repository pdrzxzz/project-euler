def sum_of_k_multiples_up_to_n(k, n):
    qtd_multiples = (n - 1) // k
    return k * qtd_multiples * (qtd_multiples+1) // 2

n = 1000
total = sum_of_k_multiples_up_to_n(3, n) + sum_of_k_multiples_up_to_n(5, n) - sum_of_k_multiples_up_to_n(15, n)
print(total)
