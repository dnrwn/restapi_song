젠킨스 재구축

예정
1. jenkins job 수정
- github_testscript > restapi workspace와 병합하는 방식으로
- 바로 clone하지 않고 testcase 디렉토리 생성해서 clone
  - 추후 더 좋은 방안 조사 필요
- 완료 후 notion에 작성한 CI/CD 포트폴리오 수정
- 디렉토리 만들고 다시 그 파이프라인을 타면 이미 디렉토리가 있다는 error 발생
  - 예외처리 필요

2. 유닛 테스트용 Test Script 추가
- 대상 : Query.py, main.py (db.py 제외)
  - 유닛 테스트의 경우 server를 통하지 않고 직접 소스에 접근하는 개념으로 하기 때문에 db return을 만들어서 테스트하기엔 db에 대한 숙련도가 낮아서 소요 시간이 긺

3. 새로 작성한 요구사항을 기준으로 기존에 설계한 test script도 정리 필요
- excel_read, Selenium, postman

4. Jenkins CI/CD 구축
- clone, test, deploy (build는 python 환경에서 필요 없어서 추후 c++, java 로 진행 예정) [완료]
- test의 경우 어떤 방식으로 운영할지 검토 필요 [완료]
  - 유닛테스트, 통합테스트, 셀레늄
- 배포 > deploy 절차로 docker에 dev server 구축해서 매뉴얼 테스트 환경 구성 [완료]
- 배포 > release 절차로 매뉴얼 테스트 완료 시 docker에 수동으로 배포하는 Job 구성 [완료]
- CI/CD 구축 과정들 Notion에 정리 (구축 과정, pipeline 운영법, 이슈 및 얻은 지식 등) [부분 완료]
  - Jenkins job : restapi, testscript, jenkins_C (restapi run, testscript run), jenkins_D (docker 배포), jenkins_E (docker 배포 / Release server)
    - jenkins_C에서 restapi, testscript 워크스페이스를 공유 받아서 작업을 수행하는데, pipeline에 절대 경로로 작성하였으나 유지보수 및 보안 이슈로 인해 수정 필요

5. 파일 정리
- README 파일 정리 검토 (P2)
  - 내용 정리, 통합 등 최신화
- pytest init.py 파일 위치 정리 필요 (P2)
- 포트폴리오 리뷰.pdf 파일 정리 (P3) # P2건 모두 정리된 이후 수행

6. 초기 mysql 셋업할 때 root 계정 비밀번호 생성하는 code 추가 필요
- init.sql에 root 계정의 비밀번호가 드러나 있으므로 보안 문제 해결 필요

7. db data 복호화 key / value 파일 관리 방안 검토 필요
- 현재는 server 내부에서 관리
- github를 통해 clone하고 다 사용하면 delete 하는 방식을 검토하였으나 추가 검토 필요
- mysql에 해당 기능이 있으나 조금 더 조사 필요 (mysql transparent data encryption)
- 암호화 하는 함수를 server에 내장하는건 원본 data를 server에서 가지고 있어야 하기 때문에 암호화하는 의미가 없음

2025-02-04 업데이트
1. db.py
- db connect에 필요한 data 암호화/복호화 과정 삽입
- db 함수 log 삽입
- db 예외처리 sql로 이관

2. init.sql
- db, table 없을 경우 create 하는 쿼리 삽입
- 별도 계정 생성 쿼리 삭제
- root 계정 비밀번호 설정 쿼리 삽입 (보안 관련 추가 개선 필요)

3. db data 암호화, 복호화에 대한 key, value 파일 추가
4. db.py 재구조화 (P3) # rest api server는 테스트 자동화를 위한 도구이므로 중요도 낮음 (완료 / docker로 해당 부분 간단히 해결)
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

5. 요구사항 정리
- doc 디렉토리 추가
- 기존 요구사항 : API_requirements.md
- db 함수 요구사항 : db_requirements.md
- main 함수 요구사항 : server_requirements.md
- ui 요구사항 : ui_requirements.md

6. jenkins job 수정
- workspace에 바로 clone 하지 않고 restapi 디렉토리 추가해서 clone (github_restapi)
- 현재 숙련도로썬 유닛테스트용 케이스를 소스에 직접 사용하는게 용이함 (추후 다른 방법 조사)

7. requirements.txt에 추가 모듈 삽입
- cryptography.fernet==1.0.1

2025-02-03 업데이트
1. main.py
- 유닛 테스트, 통합 테스트의 효과를 확인하기 위해 구조 변경
  - Route 함수와 Logic 함수 분리
  - Select, Update 가 한 함수에서 if로 관리되던 것을 각각의 함수로 분리 (html 수정 포함)

2025-01-30 업데이트
1. 리포지토리 브랜치 이름 변경
- 이슈 : github에서 webhook 로그가 정상 (200) 으로 보내지고 jenkins에서 hook log가 출력되는데 파이프라인 트리거가 되질 않음
- 해결 : 브랜치 이름이 25-01-28로 되어 있었는데 master로 바꾸고 난 뒤에는 파이프라인 트리거 잘 됨
2. docker에서 flask가 실행되지 않음
- 원인1
  - db가 시작되기 전에 flask를 구동하려고 하면 error 발생
  - 해결 : wait sh 파일을 통해 60초간 db 상태를 체크해서 flask를 구동하도록 dockerfile 반영
- 원인2 
  - wait-for-it.sh 파일이 linux에서 사용되기 위해 줄바꿈 형식을 LF로 설정할 필요가 있음
  - github로 push될 때까지만 해도 해당 설정이 유지되는데
  - jenkins에서 clone하고 image로 빌드하는 과정에서 해당 설정이 CRLF로 변경됨
  - 개발 환경의 git 설정을 변경해도 해결 안됨 (git config --global core.autocrlf false)
  - github 리포지토리에 lf 설정을 적용하는 .gitattributes 파일을 추가해도 해결 안됨
  - 해결 : 젠킨스 워크스페이스 초기화 후 해결 확인
  - git config인지, .gitattributes 파일 때문인지, 기존 워크스페이스에 있는 파일에 덮어쓰기가 되지 않고 무시돼서 발생한 문제인지 해결 포인트 못찾음


2025-01-29 업데이트
- docker 환경에서 구동될 수 있도록 config file 추가
  - rest api : config.ini (ip, port, path)
  - db : mysql.cnf, init.sql (계정 생성)
    - init.sql은 추후에 삭제 검토 (root 계정만 사용해서 다른 계정 생성할 필요 없어 보임)
- docker build 시 필요한 yml 파일 추가
  - db, server 정보 작성 및 해당 정보로 서버 구동
- docker에서 실행할 경우 flask로 구동 중인 web app에 진입 안되는 이슈 해결
  - 0.0.0.0으로 진입이 되질 않아서 default page에 진입한 ip, port를 이어서 사용하는 code 추가 (request.host)
- docker에서 nodejs server도 구동되도록 compose file 추가

2025-01-28 업데이트
github webhooks -> jenkins pipeline 연동

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
