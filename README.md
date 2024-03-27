1. Postman -> REST API Server -> mySQL
2. REST API Server
    - Insert, Update, Select 
3. mySQL
    - Create DB, Insert, Update, Select
3. Postman
    - Insert, Update, Select

* https://github.com/dnrwn/postman_response_node


포트폴리오 계획서

[1] 목표 & 목적

	1. 목표 : Tester 포트폴리오 구성
	2. 목적
		(a) API Test 이해
		(b) 자동화 Test 이해

[2] 환경 구성

	1. web App (html)
	2. Rest Api Server (Flask)
	3. DB (mysql)
		= 구조 : web App <-> Server <-> DB

[3] 기능

	1. web App
		(3-1-a) Server로 보내는 Input data
		(3-1-b) Server로 보내는 기능 실행 요청
		(3-1-c) Server로 보내지는 DB 조회 요청 신호 / (삭제)
		(3-1-d) Server로부터 받는 DB data / (삭제)
		(3-1-e) Server로부터 받는 Output data
	2. Server
		(3-2-a) web App으로부터 받은 Input data 계산 + result data 생성
		(3-2-b) result data web App으로 전달
		(3-2-c) web App으로부터 받은 input data를 가공하여 DB로 전달  
		(3-2-d) web App의 요청에 의한 DB data 를 App으로 전달 / (삭제)
		(3-2-e) Forbidden Page로 이동할 경우 403 error로 예외 처리
		(3-2-f) All result Output으로 No Data를 받을 경우 예외 처리
	3. DB
		(3-3-a) Server로부터 받는 data 저장 + index 누적
			= index, input data, result data, create date, update date
	
[4] 전체 시나리오

	1. 숫자 계산
		(4-1-a) web App에 입력된 Input data를 버튼을 통해 Server로 전달
		(4-1-b) Server로 받은 Input data를 로직에 따라 계산하여 result data로 생성
		(4-1-c) DB를 조회하여 얻은 result data를 web App의 Output UI와 연결
		(4-1-d) web App의 Input data와 Server의 result data를 DB에 저장
			= DB 구조 : index, input data, result data, create date, update date
	2. DB에 저장된 data 조회
		(4-2-a) 전체 data
		(4-2-b) 특정 index / input / output
		(4-2-c) index 범위 / (삭제)
	3. DB에 저장된 data 삭제
		(4-3-a) 전체 data
		(4-3-b) 특정 index / input / output
		(4-3-c) index 범위 / (삭제)
	
[5] 테스트 방법

	1. web App에서 직접 Test
	2. postman을 이용하여 web App 기능 Test 자동화
		(5-2-a) valid : body -> form-data로 Key, Value 전달
		(5-2-b) invalid : pre-request script를 이용하여 list형 input을 for문으로 반복 실행
		(5-2-c) http status에 따라 결과 출력 / (삭제)
	3. Selenium을 이용하여 web App 기능 Test 자동화
		(5-3-a) web App의 Input 요소를 찾고 input data 자동 입력
		(5-3-b) web App의 submit 요소를 찾고 기능 실행
		(5-3-c) web App의 Output data와 Input data (or DB data)를 assert로 비교
		(5-3-d) pytest 구조로 TC 설계
	4. pytest와 Selenium 응용하여 Test 자동화
		(5-4-a) Test Case 설계
			- assert문을 이용한 data 비교
			- Pass, Fail 처리
			- TC 반복 실행
	5. selenium 캡처 기능으로 기능 실행 전, 후 상태 이미지로 
		
[6] 테스트 시나리오

	(6-a) 시나리오 a : web App input / output 생성
		= output, input data(or DB data) 비교
	(6-b) 시나리오 b : DB 조회1 -> input (Valid / Invalid) Server로 전달 -> DB 조회2 
		= 정의된 message return check
		= DB 조회1, 2 data 비교 
	(6-c) 시나리오 c : DB 조회 (invalid / null) 
		= 정의된 message return check

[7] 계획

    1. 포트폴리오 계획서 작성 (~ 2021-07-16)​
    2. web App, Server, DB 구현 + Selenium 작성(~ 2021-07-17)​
    3. pytest 작성 + 전반적인 보강 (~ 2021-07-18)​
    4. 포트폴리오 완료 (2021-07-21)
	
[8] 출처 & 참조

	1. 이용 언어
		(8-1-a) python
		(8-1-b) http
		(8-1-c) javascript
		(8-1-d) css
		(8-1-e) mysql 제어문
	2. open API
		(8-2-a) Flask
		(8-2-b) pytest
		(8-2-c) selenium
		(8-2-d) datetime
		(8-2-e) pymysql
	3. Tool
		(8-3-a) PyCharm
		(8-3-b) mysql
	4. webdriver
		(8-4-a) chromedriver
		(8-4-b) edgedriver
	5. 출처
		- flask, html 연동 : https://kkamikoon.tistory.com/155?category=825129
		- mysql, server 연동 : https://kkamikoon.tistory.com/156
		- flask, html input 송수신 : https://roksf0130.tistory.com/100
		- html tab UI : https://imivory.tistory.com/8
		- postman에서 javascritp로 TC 작성 : https://gist.github.com/dariayermolova/450e83f03d15b5c8b34f922e386d8825
		- 디렉토리 유무 체크 후 생성 : https://devpouch.tistory.com/139
		- Selenium 캡쳐 : https://cozynow.tistory.com/41


[9] 사용법

	1. Server 구동
		(9-1-a) run.py 실행
	2. 경로
		(9-2-a) server : app/test/test.py
		(9-2-b) selenium : app/postman_test_selenium.py
		(9-2-c) postman :  app/postman/test_postman.josn
		(9-2-c) html : app/templates/test/test_test.html
	3. Selenium 실행
		(9-3-a) terminal에서 app/selenium 디렉토리 진입
		(9-3-b) pytest test_selenium 입력 후 실행
	4. Postman
		(9-4-a) app/postman/test_postman.json 파일을 Postman Tool에서 import
		(9-4-b) Postman Tool > Collections에서 import된 Collections의 우측 ... 버튼 선택 > Run collection 버튼 선택
		(9-4-c) run test_postman copy 버튼 선택
	5. 이미지 저장 경로
		(9-5-a) .../selenium/{test 시작 시간}/insert(or update, select, delete)/
