import requests
print(requests.__version__)
requests.get("http://google.com")
print(requests.get("https://raw.githubusercontent.com/archit-soni/404Lab1/main/lab1.py").content)
