이슈
docker 컨테이너에서 실행하면 mysql 에서 error 발생함
- mysql 설치하고 초기 세팅하는 부분이 생략돼서 그런듯
- mysql에서 db table이 없을 경우 추가하는 script는 있는데 계정 생성하는 부분이 없어서 그런듯 


예정 
- README 파일 정리 검토 (P2)
  - 내용 정리, 통합 등 최신화
- pytest init.py 파일 위치 정리 필요 (P2)
- 포트폴리오 리뷰.pdf 파일 정리 (P3) # P2건 모두 정리된 이후 수행
- db.py 재구조화 (P3) # rest api server는 테스트 자동화를 위한 도구이므로 중요도 낮음
    - 현재 : db create, execute 코드만 만 작성되어 있음
    - 변경 : 관리 및 유지보수 측면에서 독립적으로 구동되는 db로 재구조화할 필요 있음
        - db_run.py (예)
            - mysql install
                - install + windows service 추가
            - mysql uninstall
                - uninstall + windows service 삭제
            - db create
                - connection info 포함
        - db_execute.py (예)
            - execute 기능만 있는 별도 모듈로 재구조화
        - service_script.py
            - mysql, nodjs windows service 컨트롤 script
              - nodejs server를 windows 서비스에 등록하는 script 작성 (bat)

2025-01-28 업데이트
github webhooks -> jenkins pipeline 연동
-=

2025-01-22 업데이트
- excel_read, rest api server 이원화
  - app 하위에 있는 자동화 script는 excel_read 쪽으로 통합하여 자동화로 카테고리 변경
  - nodejs server를 postman과 관리될 수 있도록 통합
  - Query.py 파일 위치 변경 (db_f 하위)
  - rest api server console log 수집하는 script 추가
  - print로 작성된 부분 정리 및 console log 이식
- readme 에서 요구사항 내용 분리 (requirements.md)

2025-01-20 업데이트 
- idx가 없을 경우 예외처리 추가 (db.py)

2024-04-02 업데이트
- Selenium Script 초안 작성 완료
  - pytest 사용해서 test 결과 report 하도록 작성, 
  - 각 Case별 submit 버튼 선택 전/후 각 screen capture 동작 작성

2024-04-01 업데이트
- 기존 : main.py 에서 postman evnet 만 대응
- 변경 : html 파일 추가, main 에서 html request 추가 대응, node 경로 변경, main README.md 수정

2024-03-29 업데이트
- 기존 : main.py 에서 Postman data 를 가공해서 Query.py에 전달
  - 전달 값의 [필수, 선택] 성격을 함수 인자로 부여
- 변경 : main.py 에서 Postman data 를 가공하지 않고 그대로 Query.py에 전달
  - Query.py 에서 query 가공
    - 필수 > Dict 내 key 값으로 value 호출
    - 선택 > .get 기능을 통해 예외 처리


########################################
구조 요약
1. test_script -> REST API Server -> mySQL -> REST API Server
   - test_script = postman, selenium, python_requests
2. REST API Server
    - Insert, Update, Select, Delete
3. mySQL
    - Create DB, Insert, Update, Select, Delete


포트폴리오 계획서

[1] 목표 & 목적

	1. 목표 : Tester 포트폴리오 구성
	2. 목적
		(a) API Test 이해
		(b) 자동화 Test 이해

[2] 환경 구성

	1. App (html, Postman)
	2. Rest Api Server (Flask)
	3. DB (mysql)
		= 구조 : App <-> Server <-> DB

[3] 기능

	1. Server
		(3-1-a) Server가 App으로부터 전달받은 Input data를 query 형태로 변환
        (3-1-b) Server가 query 형태의 Message를 DB에 전달
        (3-1-c) Server가 실행 결과를 App에 전달
	2. DB
        (3-2-a) DB가 전달 받은 Message를 실행
    3. App
        (3-3-a) App에서 기능 선택 및 입력한 Input data 값을 Server로 전달
        (3-3-b) App이 Server로부터 전달받은 실행 결과를 출력

[4] 테스트 방법

	1. App에서 직접 Test
	2. postman을 이용하여 App 기능 Test 자동화
		(5-2-a) valid : body -> form-data로 Key, Value 전달
		(5-2-b) invalid : pre-request script를 이용하여 list형 input을 for문으로 반복 실행
		(5-2-c) http status에 따라 결과 출력 / (삭제)
	3. Selenium을 이용하여 App 기능 Test 자동화
		(5-3-a) App의 Input 요소를 찾고 input data 자동 입력
		(5-3-b) App의 submit 요소를 찾고 기능 실행
		(5-3-c) App의 Output data와 Input data (or DB data)를 assert로 비교
		(5-3-d) pytest 구조로 TC 설계
	4. pytest와 Selenium 응용하여 Test 자동화
		(5-4-a) Test Case 설계
			- assert문을 이용한 data 비교
			- Pass, Fail 처리
			- TC 반복 실행
	5. selenium 캡처 기능으로 기능 실행 전, 후 상태 이미지로 

[5] 출처 & 참조

	1. 이용 언어
		(6-1-a) python
		(6-1-b) http
		(6-1-c) javascript
		(6-1-d) mysql 제어문
	2. open source 
		(6-2-a) Flask
		(6-2-b) pytest
		(6-2-c) selenium
		(6-2-d) datetime
		(6-2-e) pymysql
	3. Tool
		(6-3-a) PyCharm
		(6-3-b) mysql
	4. webdriver
		(6-4-a) chromedriver
		(6-4-b) edgedriver
	5. 출처
		- flask, html 연동 : https://kkamikoon.tistory.com/155?category=825129
		- mysql, server 연동 : https://kkamikoon.tistory.com/156
		- flask, html input 송수신 : https://roksf0130.tistory.com/100
		- html tab UI : https://imivory.tistory.com/8
		- postman에서 javascritp로 TC 작성 : https://gist.github.com/dariayermolova/450e83f03d15b5c8b34f922e386d8825
		- 디렉토리 유무 체크 후 생성 : https://devpouch.tistory.com/139
		- Selenium 캡쳐 : https://cozynow.tistory.com/41

[6] 사용법

	1. Server 구동
		(7-1-a) main.py 실행
	2. 경로
		(7-2-a) Server : server/main.py
		(7-2-b) Selenium : app/Selenium/postman_test_selenium.py
		(7-2-c) Postman :  app/postman/postman_item.josn
		(7-2-d) html : server/templates/test_test.html
        (7-2-e) Node : postman_response_node/ postman_response_node_v1.4.0
	3. Selenium 실행
		(7-3-a) terminal에서 app/selenium 디렉토리 진입
		(7-3-b) pytest selenium_script.py > 5.console_log/log.log 입력 후 실행
        (7-3-c) 이미지 저장 경로 : ../selenium/{test 시작 시간}/insert(or update, select, delete)/..in(or out).png
	4. Postman 실행
		(7-4-a) app/postman/postman_item.josn 파일을 Postman Tool에서 import
		(7-4-b) Postman Tool > Collections에서 import된 Collections의 우측 ... 버튼 선택 > Run collection 버튼 선택
	5. Node
        (7-5-a) server 실행 시 Node Server 자동 실행 // server/node.py 
        (7-5-b) Save File 저장 경로 : server/test/...
