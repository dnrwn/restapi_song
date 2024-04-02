import requests
import file_read

run = file_read.FUNC()
case = run.input_add_json()

case_item = case['item']
case_result = case['result']


def insert_case():
    for i in range(len(case_item)):
        j = case_item[f'case_{i+1}']
        if j['function_name'] == 'Insert':
            print(j)
            get_result = requests.post(url='http://localhost:70/func_2', json=j)
            print(get_result)
        elif j['function_name'] == 'Select':
            print(j)
            get_result = requests.get(url='http://localhost:70/func_1', json=j)
            print(get_result)
        elif j['function_name'] == 'Update':
            print(j)
            get_result = requests.post(url='http://localhost:70/func_1', json=j)
            print(get_result)
        elif j['function_name'] == 'Delete':
            print(j)
            get_result = requests.post(url='http://localhost:70/func_3', json=j)
            print(get_result)


insert_case()
