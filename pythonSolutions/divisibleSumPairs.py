def divisibleSumPairs(n, k, ar)-> int:
    num_of_pairs = 0
    for i in range(0,n):
        for j in range(0,n):
            if i != j:
                sum = ar[i] + ar[j]
                if i < j and sum and not sum % k:
                    num_of_pairs += 1
    return num_of_pairs

ar = [1,2,3,4,5,6]
print(divisibleSumPairs(len(ar),5,ar))