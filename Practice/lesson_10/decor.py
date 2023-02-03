def decorator(func):
    import time

    def wrapper(url):
        start = time.time()
        response = func(url)
        end = time.time()
        print(f"Ваше время {end - start}")
        return response
    return wrapper


@decorator
def request(url):
    import requests
    response = requests.get(url)
    return response


print(request("https://ya.ru"))
