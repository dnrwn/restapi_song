# db.py, Query.py Unit Test용 요구사항

## 목차
- [init](#init)
- [execute](#execute)

# Database

## init
- **Input**

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| host      | -      | Mandatory | 1. IP : (string) </br> 2. user : (string) </br> 3. password : (string) </br> 4. charset : (string) </br> 5. port : (init) |

- **Output**
- 결과 : database와 통신할 수 있는 환경 조성

## execute

- **Input**
- 조건: __init__을 통해 DB Connect 가능한 상태

| Parameter | Type   | Required  | Description    |
|-----------|--------|-----------|----------------|
| query     | string (SQL) | Mandatory | Query.py 참조 |

- **Output**
- 결과 : select * from database_name.table_name; 과 같음

| idx | input_1 | input_2 | input_3 | input_4 | Create_date       | Update_date |
|-----|---------|---------|---------|---------|-------------------|-------------|
| 1   | 1       | 1       | 1       | 1       | 25-02-03 11:38:13 | NULL        |

# Query
- 참조
  - Query 요구사항에 Table row의 Type length 정보를 제공하지 않는 이유는, server나 db 소스에서 length를 제한하는 코드가 없으므로 mysql 자체의 제한에 의존하기 때문
  - Type (자료형) 자체에 대한 제한은 있음
- 제약사항 : Table row length에 대한 Test는 다음 쿼리로 의존/대체
  - SHOW COLUMNS FROM new_db.item;
- 추후 개선 예정

## date
- **Input**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| -         | -    | -        | -           |

- **Output**
- Time format : yyyy-mm-dd HH:MM:SS

## get_select_all
- **Input**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| -         | -    | -        | -           |

- **Output**
- string (SQL) : "SELECT * FROM new_db.item;"

## get_select_one
- **Input**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query     | dict | Mandatory | idx         |
| query.idx | int  | Mandatory | idx : (int) |

- **Output**
- string (SQL) : "SELECT * FROM new_db.item where idx = [idx];"

## post_insert
- **Input**

| Parameter        | Type   | Required | Description       |
|------------------|--------|----------|-------------------|
| query            | dict   | Mandatory | input_1, input_2, input_3, input_4, create_date |
| query.input_1    | int    | Mandatory | input_1 : (int)  |
| query.input_2    | string | Mandatory | input_2 : (string)  |
| query.input_3    | string | Mandatory | input_3 : (string)  |
| query.input_4    | boolean| Mandatory | input_4 : (int)   |
| query.create_data| time   | Mandatory | create_data : (string) |

- **Output**
- string (SQL) : "SELECT * FROM new_db.item where idx = [idx];"

## post_update
- **Input**

| Parameter        | Type   | Required | Description       |
|------------------|--------|----------|-------------------|
| query            | dict   | Mandatory | input_1, input_2, input_3, input_4, create_date, idx |
| query.input_1    | int    | Mandatory | input_1 : (int)  |
| query.input_2    | string | Mandatory | input_2 : (string)  |
| query.input_3    | string | Mandatory | input_3 : (string)  |
| query.input_4    | boolean| Mandatory | input_4 : (int)   |
| query.update_data| time   | Mandatory | update_data : (string) |
| query.idx        | int    | Mandatory | idx : (int) |

- **Output**
- string (SQL) : "UPDATE item SET input_1=[input_1], input_2='[input_2]', input_3='[input_3]', input_4=[input_4], update_date='[update_data]' WHERE idx = [idx];"

## delete_delete
- **Input**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query     | dict | Mandatory | idx         |
| query.idx | int  | Mandatory | idx : (int) |

- **Output**
- string (SQL) : "DELETE FROM new_db.item where idx=[idx];"
