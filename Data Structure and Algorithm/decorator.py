def cache(func):
    cache_dict= {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in  cache_dict:
            return cache_dict[key]
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    return wrapper
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
    
    
    
        