
def friendCircles(friends):
    sets = []
    for i in range(0, len(friends)):
        sets.append(friends[i])

    for i in range(1, len(friends)):
        for j in range(0, i):
            if (friends[i][j]) == "Y":
                sets[make_sets(i, sets)] = make_sets(j, sets)

    res = set([])
    for i in range(0, len(friends)):
        res.add(make_sets(i, sets))
    return len(res)


def make_sets(node, sets):
    while sets[node] != node:
        sets[node] = sets[sets[node]]
        node = sets[node]
    return node

matrix = [['Y','Y','N','N'],['Y','Y','Y','N'],['N','Y','Y','N'],['N','N','N','Y']]

friendCircles(matrix)

def longestChain(words):
    # Write your code here
    dp = {}
    for w in sorted(words, key=len):
        dp[w] = max(dp.get(w[:i] + w[i+1:],0) + 1 for i in range(len(w)))
    return max(dp.values())
