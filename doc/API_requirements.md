값의 범위에 대한 예외 처리 -> db.py
값 Required에 대한 예외 처리 -> main.py

########################################
기능 요구사항
1. Select // Method : GET
- input

| Parameter | type |Required| Description   |
|-----------|------|---|---------------|
| idx       | int  |Mandatory| 조회할 idx 필수 입력 |

- output

| Fild        | Type   | Description                                                                                                                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result      | String | - PASS </br> - NG </br> - Error </br>                                                                                                                                                           |
| Description | String | - NG : Select NG </br> - Error : Null                                                                                                                                                         |
| Message     | String | - NG : Exception Message                                                                                                                                                                      |
| Data        | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : int </br> }] |

2. Update // Method : POST
- input

| Parameter | type    | Required  | Description                   |
|----|---------|-----------|-------------------------------|
| idx | int     | Mandatory | 조회할 Idx 필수 입력                 |
| input_1 | int     | Mandatory | 범위 :   -2147483648 ~ 2147483647 |
| input_2 | String  | Optional  | 범위 : 5자리 이하                   |
| input_3 | String  | Optional  | 범위 : 10자리 이하                  |
| input_4 | Boolean | Optional  | true, false                   |

- output

| Fild        | Type   | Description                                                                                                                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result      | String | - PASS </br> - NG </br> - Error </br>                                                                                                                                                           |
| Description | String | - NG : Update NG </br> - Error : Null                                                                                                                                                         |
| Message     | String | - NG : Exception Message                                                                                                                                                                      |
| Data        | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : int </br> }] |

3. Insert // Method : POST
- input

| Parameter | type    | Required  | Description                   |
|----|---------|-----------|-------------------------------|
| input_1 | int     | Mandatory | 범위 :   -2147483648 ~ 2147483647 |
| input_2 | String  | Optional  | 범위 : 5자리 이하                   |
| input_3 | String  | Optional  | 범위 : 10자리 이하                  |
| input_4 | Boolean | Optional  | true, false                   |

- output

| Fild        | Type   | Description                                                                                                                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result      | String | - PASS </br> - NG </br> - Error </br>                                                                                                                                                           |
| Description | String | - NG : Insert NG </br> - Error : Null                                                                                                                                                         |
| Message     | String | - NG : Exception Message                                                                                                                                                                      |
| Data        | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : int </br> }] |

4. Delete // Method : DELETE
- input

| Parameter | type |Required| Description   |
|-----------|------|---|---------------|
| idx       | int  |Mandatory| 조회할 idx 필수 입력 |

- output

| Fild        | Type   | Description                           |
|-------------|--------|---------------------------------------|
| Result      | String | - PASS </br> - NG </br> - Error </br>   |
| Description | String | - NG : Delete NG </br> - Error : Null |
| Message     | String | - NG : Exception Message              |
| Data        | String | - PASS : idx                            |

########################################
