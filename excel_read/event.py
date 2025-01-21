import requests
import file_read
import json

# function_name, method, url 정보 관리 위치 검토 필요
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
    if a == 1:
        for i in range(len(case_item)):
            case_id = f'case_{i+1}'
            case_item_select = case_item[case_id]
            case_result_select = case_result[case_id]
            print(case_id)
            # key = function_name, item = method, url
            for key, item in func_item.items():
                if case_item_select['function_name'] == key:
                    if item['method'] == 'post':
                        response = requests.post(url=item['url'], json=case_item_select)
                    elif item['method'] == 'get':
                        response = requests.get(url=item['url'], json=case_item_select)
                    else:
                        raise ValueError ('method Error')

                    ## write 함수 호출
                    if case_result_select['Expected_result'] == response.json()['Result']:
                        run.test_result_write(case_result_select['Actual_result'], case_result_select['record'], 'PASS')
                    else:

                        run.test_result_write(case_result_select['Actual_result'], case_result_select['record'], response.json()['Result'],
                                              record=(response.json()['Description'], response.json()['Message']))
                else:
                    pass
    # Case 선별 실행
    elif a != 1:
        case_item_select = case_item['case_5']
        if case_item_select['function_name']:
            print(case_item_select)
            response = requests.post(url='http://localhost:70/func_1', json=case_item_select)
            print(response.json())


if __name__ == "__main__":
    case_run()