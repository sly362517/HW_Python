def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


#params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
#print(params)
