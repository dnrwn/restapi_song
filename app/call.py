import requests

url = "http://192.168.68.58:70"


def select_case_1():
    a = requests.get(url=url+'/func_1', params={
        "idx": "1"
    })

    return a.json()


def select_case_2():
    a = requests.get(url=url+'/func_1')

    return a.json()

print(select_case_2())