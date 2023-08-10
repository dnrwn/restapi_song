import requests

url = "http://192.168.68.58:70"


def select_case_1():
    a = requests.get(url=url+'/func_1', params={
        "idx": "4"
    })

    return a.json()


def select_case_2():
    a = requests.get(url=url+'/func_1')

    return a.json()


def insert_case_1():
    a = requests.post(url=url+'/func_2', params={
        "input_1": "1",
        "input_2": "2",
        "create_date": "2023-08-10 13:08:00"
    })
    return a.content


def insert_case_2():
    a = requests.post(url=url+'/func_2', params={
        "input_1": "1"
    })
    return a.json()


def insert_case_3():
    a = requests.post(url=url+'/func_2', params={
        "input_2": "1"
    })
    return a.json()


def update_case_1():
    a = requests.post(url=url+'/func_1', params={
        "idx": "4",
        "input_1": "abcde",
        "input_2": "bbbbb"
    })
    return a.json()


def update_case_2():
    a = requests.post(url=url+'/func_1', params={
        "input_1": "aalskjda",
        "input_2": "asdlkjas"
    })
    return a.json()


print(update_case_1())