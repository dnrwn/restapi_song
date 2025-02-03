## 목차
- [1](#1) : 초기 화면
- [2](#2) : test app 화면
- [3](#3) : Insert tab 선택 화면
  - [3-1](#3-1) : Insert 결과 화면
- [4](#4) : Select tab 선택 화면
  - [4-1](#4-1) : Select 결과 화면
- [5](#5) : Insert tab 선택 화면
  - [5-1](#5-1) : Insert 결과 화면
- [6](#6) : Select tab 선택 화면
  - [6-1[](#6-1) : Select 결과 화면

### 1
![1](https://github.com/user-attachments/assets/cd8f7eee-9245-4a5f-86ab-e1ca07727c1b)
- 각 기능을 Direct로 Request 할 수 있는 Link
  - Select, Update, Insert, Delete
  - Parameter, body 값은 empty 상태로, Error Return
- test App 진입 Link

### 2
![2](https://github.com/user-attachments/assets/d2e7ba34-7dc0-4cac-a029-731a805871cd)
- Test App Link 진입 시 보이는 화면
- title : test app
- Default
  - tabs Show (INSERT, SELECT, UPDATE, DELETE)
  - tab-content hide
 
### 3
![3](https://github.com/user-attachments/assets/118d84f4-2aad-4552-a6ff-6cc2f225c6a9)
- Insert tab 선택 시 보이는 화면
- Title 유지
- Insert tab-content show (input_1, input_2, input_3, input_4)
  - UI 제약 사항 없음
- submit : tab-content의 Input field에 입력한 data를 REST API Server로 전달
  - DB에 idx를 증분하고 해당 idx에 input_1, input_2, input_3, input_4 값이 저장
  - submit 버튼 선택한 시점을 create_date로 DB에 저장

## 3-1
![3-1](https://github.com/user-attachments/assets/2fe1698a-5a1e-46a1-9669-2e08392ac51b)
- Insert 실행에 대한 Response 출력

### 4
![4](https://github.com/user-attachments/assets/b2a79dc1-7f39-4bad-8e5b-7a5e9d3af67b)
- Select tab 선택 시 보이는 화면
- Title 유지
- Select tab-content show (index)
  - UI 제약 사항 없음
- submit : tab-content의 Input field에 입력한 data를 REST API Server로 전달
  - DB에서 index로 입력한 data 조회

## 4-1
![4-1](https://github.com/user-attachments/assets/255fbb9b-3c90-45d9-ae4b-68fd6236bbd1)
- Select 실행에 대한 Response 출력

### 5
![5](https://github.com/user-attachments/assets/a1438889-cbc2-4595-b865-e77b9187d8ec)
- Update tab 선택 시 보이는 화면
- Title 유지
- Update tab-content show (index, input_1, input_2, input_3, input_4)
  - UI 제약 사항 없음
- submit : tab-content의 Input field에 입력한 data를 REST API Server로 전달
  - 입력한 input data를 입력한 idx에 저장
  - submit 버튼 선택한 시점을 update_date로 DB에 저장

## 5-1
![5-1](https://github.com/user-attachments/assets/497a0cdc-b7fa-47ef-8da3-a62e3919d96a)
- Update 실행에 대한 Response 출력


### 6
![6](https://github.com/user-attachments/assets/85478d2a-0b67-45cb-861a-ac553d160603)
- Delete tab 선택 시 보이는 화면
- Title 유지
- Delete tab-content show (index)
  - UI 제약 사항 없음
- submit : tab-content의 Input field에 입력한 data를 REST API Server로 전달
  - DB에서 index로 입력한 data 삭제

## 6-1
![6-1](https://github.com/user-attachments/assets/47237cfd-2142-4839-96be-e77c335357f9)
- Delete 실행에 대한 Response 출력
