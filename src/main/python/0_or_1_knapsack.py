def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    print ("----------------")
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif wt[i-1] <= j:
                K[i][j] = max(val[i-1] + K[i-1][j-wt[i-1]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    for i in range(n+1):
        for j in range (W+1):
            print('{:4}'.format(K[i][j]), end='')
        print("\n")
    return K[n][W]

# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))