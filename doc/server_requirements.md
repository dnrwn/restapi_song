# main.py Unit Test용 요구사항

## 목차
- [Common](#1-common)
  - [Response](#1-1-response)
- [Route](#2-route)
  - [route_default](#2-1-route_default)
  - [route_ui](#2-2-route_ui)
  - [route_func_1](#2-3-route_func_1)
  - [route_func_2](#2-4.route_func_2)
  - [route_func_3](#2-5.route_func_3)
  - [route_func_4](#2-6.route_func_4)
- [Logic](#3-logic)
  - [logic_default](#3-1-logic_default)
  - [logic_ui](#3-2-logic_ui)
  - [logic_select](#3-3-logic_select)
  - [logic_update](#3-4.logic_update)
  - [logic_insert](#3-5.logic_insert)
  - [logic_delete](#3-6.logic_delete)

# 1-Common

## 1-1-Response
- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| a         | int    | Mandatory | 0, 1, else     |
| b         | string | Optional  | default = None |
| c         | string | Optional  | default= None  |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

# 2-Route

## 2-1-route_default

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| rule  | string      |   Mandatory       | rule : '/'              |
| method  | stirng      |   Mandatory       | methods = 'GET'         |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  - Dicrect Request : Insert, Select, Update, Delete 하이퍼링크 제공 </br>- UI 하이퍼링크 제공 | 

## 2-2-route_ui

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| rule  | string      |   Mandatory       | rule : '/ui'              |
| method  | stirng      |   Optional       | methods 무관      |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  UI App 실행 | 

## 2-3-route_func_1

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| rule  | string      |   Mandatory       | rule : '/func_1'              |
| method  | stirng      |   Mandatory       | methods = 'GET'         |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  Select Request 실행 | 

## 2-4.route_func_2

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| rule  | string      |   Mandatory       | rule : '/func_2'              |
| method  | stirng      |   Mandatory       | methods = 'POST'         |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  Update Request 실행 | 

## 2-5.route_func_3

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| rule  | string      |   Mandatory       | rule : '/func_3'              |
| method  | stirng      |   Mandatory       | methods = 'POST'         |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  Insert Request 실행 | 

## 2-6.route_func_4

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| rule  | string      |   Mandatory       | rule : '/func_1'              |
| method  | stirng      |   Mandatory       | methods = 'POST', 'DELETE'         |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  Delete Request 실행 | 

# 3-Logic

## 3-1logic_default

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| route_data         | string      |    Mandatory      | IP, Port 구조 </br> -1-1-1-1:99              |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  [route_default](#route_default)와 동일 | 

## 3-2-logic_ui

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| route_data         | string      |    Optional      | App File Name </br> - Default : test_test.html              |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  [route_ui](#route_ui)와 동일 | 


## 3-3-logic_select

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| route_data         | dcit      |    Mandatory      | idx : (int) |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  [route_select](#route_select)와 동일 | 

## 3-4.logic_update

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| route_data         | dcit      |    Mandatory      | 1- form data </br> - idx: (int)</br> - input_1 : (int)</br> - input_2</br> - input_3</br> - input_4 : (bool)  </br> 2- json </br> - idx : (int)</br> - input_1 : (int)</br> - input_2</br> - input_3</br> - input_4 : (bool) |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  [route_update](#route_update)와 동일 | 

## 3-5.logic_insert


- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| route_data         | dcit      |    Mandatory      | 1- form data </br> - input_1 : (int)</br> - input_2</br> - input_3</br> - input_4 : (bool)  </br> 2- json </br> - input_1 : (int)</br> - input_2</br> - input_3</br> - input_4 : (bool) |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  [route_insert](#route_insert)와 동일 | 

## 3-6.logic_delete

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| route_data         | dcit      |    Mandatory      | 1- POST, form data </br> - idx : (int) </br> 2- DELETE, json </br> - idx : (int) |

- **Output**

| Field        | Type   | Description|
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return       | - |  [route_delete](#route_delete)와 동일 | 
