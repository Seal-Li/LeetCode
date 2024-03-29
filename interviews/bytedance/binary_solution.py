def func(x):
    return x ** 2 - 2

def binary_search_root(func, a, b, tol=1e-6, max_iter=1000):
    if func(a) == 0:
        return a
    if func(b) == 0:
        return b

    it = 0
    
    while it < max_iter:

        middle = (a + b) / 2
        
        if abs(func(middle)) < tol:
            return middle

        if func(a) * func(middle) < 0:
            b = middle
        else:
            a = middle
        
        it += 1
    
    print("Maximum iterations reached.")
    return middle

print(binary_search_root(func, 0, 2, tol=1e-6, max_iter=1000))
