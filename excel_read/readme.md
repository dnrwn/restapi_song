해야할 일
- 첫 열로 얻은 값을 key로 지정하고 두 번째 열부터 얻은 각 행의 data와 같이 json 형태로 가공
- 가공된 data를 server api로 push 하는 동작 추가


version : 0.3, date : 2024-03-30
- main -> file_read 파일명 변경
- event -> GET, POST in/out Event 생성 (Postman 대응)
- 주요 변경 사항
  - 기존 : globals 함수를 통해 python script 로 테스트 결과 생성
  - 변경 : Excel 의 각 cell 값을 GET, POST 형태로 전달 (func_connect() 함수 수정)
- input 을 통해 if 문으로 tkinker 사용 시 탐색기 시작되지 않고 프리징 현상 발생하여 File 수동 선택하도록 작성


version : 0.2.1, date : 2023-09-07
- python tc, function 부분 분리 (미완)
- main script 보완

개요 : 엑셀 문서로 작성된 TC와 Python Script로 작성된 TC를 통해 API 기능 실행 결과를 기록하는 로직 작성

1. 구성
- TC.xlsx : TC 예시 문서
- main.py : TC 문서 data를 동적 변수에 삽입, 삽입된 변수를 py_tc.py 의 함수에 전달, py_tc.py의 return 값을 TC 문서에 기록
- py_tc.py : main.py를 통해 TC 문서에서 얻은 data를 func.py로 전달, func.py의 return 값을 main.py로 전달
- func.py : 임시 기능부

2. Test Case (TC.xlsx) : 엑셀 파일의 행을 기준으로 아래의 Test item 작성
- Function name
- No
- description

[comment]: <> (- valid, Invalid, 해당 값으로 인해 영향을 주는 로직 없음)
- type
- Parameter
- Expected Result

3. Main 로직 (main.py) : TC.xlsx의 Item 을 읽고 동적 변수에 삽입
- Function Name : py_tc.py의 함수명을 호출하기 위해 삽입
- Parameter : py_tc.py의 인자로 삽입하기 위해 삽입

4. Test Case (py_tc.py) : main으로부터 전달받은 data를 func.py에 전달

[comment]: <> (- 동적 변수를 통해 얻은 valid, invalid 값으로 result 를 분개한다. &#40;if 문, try 문&#41;)
- 동적 변수를 통해 얻은 parameter 를 func.py에 전달(다중 인자 활용 업데이트 필요)
- func.py의 return 결과를 main.py로 전달

5. Test Case 수행 결과 (TC.xlsx)
- 엑셀 파일의 result 열에 수행 결과 입력 후 새로운 파일로 저장한다.

※ main.py와 main_2.py 차이 : 파일 선택, 읽기, 쓰기 등 각 기능 모듈화 계획이 main, 초기 계획이 main_2 

================
5. 2차 계획
- main.py : parameter cell의 data가 쉼표(,) 로 구분될 경우 parameter 분리 code 추가
  -> 복수의 parameter 입력 대응