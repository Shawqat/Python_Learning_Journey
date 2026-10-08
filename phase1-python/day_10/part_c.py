import requests


# testing with two links : 
# "https://reqres.in/api/users"
# "https://jsonplaceholder.typicode.com/todos/1"

url_one = "https://reqres.in/api/users"
url_two = "https://jsonplaceholder.typicode.com/todos/1"

def check_site(url, key):
    try :
        response = requests.get(url, timeout=10)
        print(response.status_code)      # 200
        data = response.json()           # parsed into a Python dictionary
        print(data.get(key,f"no {key}"))
    except requests.exceptions.RequestException as e :
        print(f"Request failed: {e}")

check_site(url_one, "data")
check_site(url_two, "title")