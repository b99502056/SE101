
def rotation(l,k):
    n = len(l)
    k = k % n

    former = l[0:n-k]
    latter = l[n-k:n]

    return latter + former