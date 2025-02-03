# 요구사항 문서

## 목차
- [Common](#common)
  - [Response](#response)
- [Route](#route)
  - [route_default](#route_default)
  - [route_ui](#route_ui)
  - [route_func_1](#route_func_1)
  - [route_func_2](#route_func_2)
  - [route_func_3](#route_func_3)
  - [route_func_4](#route_func_4)
- [Logic](#logic)
  - [logic_default](#logic_default)
  - [logic_ui](#logic_ui)
  - [logic_select](#logic_select)
  - [logic_update](#logic_update)
  - [logic_insert](#logic_insert)
  - [logic_delete](#logic_delete)

# Common

## Response
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

# Route

## route_default

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| -         | -      | -         | -              |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## route_ui

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| -         | -      | -         | -              |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## route_func_1

- **Input**

| Parameter | Type   | Required  | Description |
|-----------|--------|-----------|-------------|
| idx       | int    | Mandatory | index value |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## route_func_2

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| idx       | int    | Mandatory | index value    |
| input_1   | int    | Mandatory | input value 1  |
| input_4   | int    | Mandatory | input value 4  |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## route_func_3

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| input_1   | int    | Mandatory | input value 1  |
| input_4   | int    | Mandatory | input value 4  |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## route_func_4

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| idx       | int    | Mandatory | index value    |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

# Logic

## logic_default

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| -         | -      | -         | -              |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## logic_ui

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| -         | -      | -         | -              |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## logic_select

- **Input**

| Parameter | Type   | Required  | Description |
|-----------|--------|-----------|-------------|
| idx       | int    | Mandatory | index value |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## logic_update

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| idx       | int    | Mandatory | index value    |
| input_1   | int    | Mandatory | input value 1  |
| input_4   | int    | Mandatory | input value 4  |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## logic_insert

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| input_1   | int    | Mandatory | input value 1  |
| input_4   | int    | Mandatory | input value 4  |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |

## logic_delete

- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| idx       | int    | Mandatory | index value    |

- **Output**

| Field        | Type   | Description                                                                                                                                                                                   |
|--------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Result       | String | - (a = 1) PASS </br> - (a = 0) NG </br> - (a = else) Error </br>                                                                                                                               |
| Description  | String | - NG : [b] NG </br> - Error : Null                                                                                                                                                            |
| Message      | String | - c                                                                                                                                                                                           |
| Data         | String | - PASS : Response (Json) </br> [{</br> Create_date : str, </br> Update_date : str, </br> idx : int, </br> input_1 : int, </br> input_2 : str, </br> input_3 : str, </br> input_4 : Boolean </br> }] |
