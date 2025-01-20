import requests
import file_read
import json

func_item = {
    "Insert" :{
        "method":"post",
        "url":"http://localhost:70/func_2"
    },
    "Select" :{
        "method":"get",
        "url":"http://localhost:70/func_1"
    },
    "Update" :{
        "method":"post",
        "url":"http://localhost:70/func_1"
    },
    "Delete" :{
        "method":"post",
        "url":"http://localhost:70/func_3"}
}
run = file_read.FUNC()
case = json.loads(run.test_item_array())

case_item = case['item']
case_result = case['result']

def case_run(a=1):
    if a==1:
        for i in range(len(case_item)):
            case_item_select = case_item[f'case_{i+1}']
            case_result_select = case_result[f'case_{i+1}']
            print(i+1)
            for key, item in func_item.items():
                if case_item_select['function_name'] == key:
                    print(case_item_select)
                    if item['method'] == 'post':
                        response = requests.post(url=item['url'], json=case_item_select)
                    elif item['method'] == 'get':
                        response = requests.get(url=item['url'], json=case_item_select)
                    else:
                        response = 'aa'
                    print(response.json())
                    if case_result_select['Expected_result'] == response.json()['Result']:
                        ## write 함수 호출
                        pass
                    else:
                        ## write 함수 호출
                        pass
                else:
                    pass
            # if case_item_select['function_name'] == 'Insert':
            #     print(case_item_select)
            #     response = requests.post(url='http://localhost:70/func_2', json=case_item_select)
            #     print(response.json())
            # elif case_item_select['function_name'] == 'Select':
            #     print(case_item_select)
            #     response = requests.get(url='http://localhost:70/func_1', json=case_item_select)
            #     print(response.json())
            #
            # elif case_item_select['function_name'] == 'Update':
            #     print(case_item_select)
            #     response = requests.post(url='http://localhost:70/func_1', json=case_item_select)
            #     print(response.json())
            # elif case_item_select['function_name'] == 'Delete':
            #     print(case_item_select)
            #     ## requests.delete 에 대한 조사 필요 (func_3의 method가 post, delete 두 개임
            #     response = requests.post(url='http://localhost:70/func_3', json=case_item_select)
            #     print(response.json())
    elif a!=1:
        case_item_select = case_item['case_5']
        if case_item_select['function_name']:
            print(case_item_select)
            response = requests.post(url='http://localhost:70/func_1', json=case_item_select)
            print(response.json())


if __name__ == "__main__":
    case_run()

