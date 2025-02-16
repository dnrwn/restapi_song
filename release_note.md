목차
- [예정](#예정)
- [업데이트](#업데이트)

# 예정
## 0. input_4에 값이 제대로 들어가지 않는 이슈 있음
- 어떤 값을 넣어도 다 1로 삽입됨
## 0. devbiuld 파이프라인 수정
- docker에 빌드한 뒤에 unittest를 수행하도록 되어 있는데, unittest 수행 후에 빌드하도록 수정 필요
## 1. 유닛 테스트용 Test Script 추가
- 대상: `Query.py`, `main.py` (`db.py` 제외)
  - 유닛 테스트의 경우 server를 통하지 않고 직접 소스에 접근하는 개념으로 하기 때문에 `db return`을 만들어서 테스트하기엔 db에 대한 숙련도가 낮아서 소요 시간이 길어짐

## 2. 새로 작성한 요구사항을 기준으로 기존에 설계한 Test Script도 정리 필요
- `excel_read`, `Selenium`, `Postman`

## 3. 파일 정리
- `README` 파일 정리 검토 (P2)
  - 내용 정리, 통합 등 최신화
- `pytest init.py` 파일 위치 정리 필요 (P2)
- `포트폴리오 리뷰.pdf` 파일 정리 (P3) # P2건 모두 정리된 이후 수행

## 4. 초기 MySQL 셋업할 때 root 계정 비밀번호 생성하는 코드 추가 필요
- `init.sql`에 root 계정의 비밀번호가 드러나 있으므로 보안 문제 해결 필요

## 5. DB Data 복호화 Key / Value 파일 관리 방안 검토 필요
- 현재는 Server 내부에서 관리
- Github를 통해 clone하고 다 사용하면 delete하는 방식을 검토하였으나 추가 검토 필요
- MySQL에 해당 기능이 있으나 조금 더 조사 필요 (`MySQL Transparent Data Encryption`)
- 암호화 하는 함수를 Server에 내장하는 건 원본 data를 Server에서 가지고 있어야 하기 때문에 암호화하는 의미가 없음

## 6. DB 쪽 로그 Import 문제 있음
- `main.py` 기준으로 자기를 import 못함
  - 경로 문제인지, 상호 참조 문제인지 검토 필요
  - DB 쪽도 Logger를 main과 공유하여 사용하길 원함
  - 안되면 DB용 logging 코드 추가 필요

# 업데이트


## 2025-02-17 업데이트
1. jenkins/testbranchupdate 파일 수정
   - 젠킨스 파이프라인에서 git push 동작 수행
   - 이슈 : git push 인증 부분에 문제 있음 (password 인증 미지원 이슈)
   - 해결 못함 추가 검토 필요

## 2025-02-07 업데이트
1. DB 인스턴스 생성하는 부분을 잘못 삭제해서 query가 보내지지 않는 문제 수정
2. input_4 type 예외처리 반영

## 2025-02-04 업데이트
1. `db.py`
- DB connect에 필요한 data 암호화/복호화 과정 삽입
- DB 함수 log 삽입
- DB 예외처리 sql로 이관

2. `init.sql`
- DB, table 없을 경우 create 하는 쿼리 삽입
- 별도 계정 생성 쿼리 삭제
- root 계정 비밀번호 설정 쿼리 삽입 (보안 관련 추가 개선 필요)

3. DB Data 암호화, 복호화에 대한 key, value 파일 추가
4. `db.py` 재구조화 (P3) # rest api server는 테스트 자동화를 위한 도구이므로 중요도 낮음 (완료 / Docker로 해당 부분 간단히 해결)
    - 현재: db create, execute 코드만 작성되어 있음
    - 변경: 관리 및 유지보수 측면에서 독립적으로 구동되는 DB로 재구조화할 필요 있음
        - `db_run.py` (예)
            - `MySQL install`
                - install + Windows service 추가
            - `MySQL uninstall`
                - uninstall + Windows service 삭제
            - `DB create`
                - connection info 포함
        - `db_execute.py` (예)
            - execute 기능만 있는 별도 모듈로 재구조화
        - `service_script.py`
            - `MySQL`, `NodeJS` Windows service 컨트롤 script
              - `NodeJS` server를 Windows 서비스에 등록하는 script 작성 (bat)

5. 요구사항 정리
- `doc` 디렉토리 추가
- 기존 요구사항: `API_requirements.md`
- DB 함수 요구사항: `db_requirements.md`
- main 함수 요구사항: `server_requirements.md`
- UI 요구사항: `ui_requirements.md`

## 6. Jenkins Job 수정
- `workspace`에 바로 clone하지 않고 `restapi` 디렉토리 추가해서 clone (`github_restapi`)
- 현재 숙련도로썬 유닛테스트용 케이스를 소스에 직접 사용하는 게 용이함 (추후 다른 방법 조사)

## 7. `requirements.txt`에 추가 모듈 삽입
- `cryptography.fernet==1.0.1`

## 8. DB Password 생성 주석 처리 후 삭제
- 주석 인식 안됨
- `--USE mysql;`
- `--UPDATE user SET authentication_string = PASSWORD('qwer1234') WHERE User = 'root';`
- `--FLUSH PRIVILEGES;`

## 2025-02-06 업데이트
1. Jenkins Pipeline 수정
- scm 형태로 변경 (pipeline 공유를 위함)
- jenkins 디렉토리에서 pipeline file 관리

2. Jenkins Job 수정
-> dev branch build 때 unittest를 같이 수행하고 testscript는 분리하는 것으로 수정
- `github_testscript`를 `restapi workspace`와 병합하는 방식으로 수정 
- 바로 clone하지 않고 `testcase` 디렉토리 생성 후 clone
  - 추후 더 좋은 방안 조사 필요
- 완료 후 `Notion`에 작성한 CI/CD 포트폴리오 수정
- 디렉토리 만들고 다시 그 파이프라인을 타면 이미 디렉토리가 있다는 error 발생
  - 예외처리 필요
 
3. Jenkins CI/CD 구축
- `clone`, `test`, `deploy` (build는 Python 환경에서 필요 없어서 추후 C++, Java로 진행 예정) **[완료]**
- test의 경우 어떤 방식으로 운영할지 검토 필요 **[완료]**
  - 유닛테스트, 통합테스트, 셀레늄
- 배포 > `deploy` 절차로 Docker에 dev server 구축해서 매뉴얼 테스트 환경 구성 **[완료]**
- 배포 > `release` 절차로 매뉴얼 테스트 완료 시 Docker에 수동으로 배포하는 Job 구성 **[완료]**
- CI/CD 구축 과정들 `Notion`에 정리 (구축 과정, pipeline 운영법, 이슈 및 얻은 지식 등) **[완료]**

## 2025-02-03 업데이트
1. `main.py`
- 유닛 테스트, 통합 테스트의 효과를 확인하기 위해 구조 변경
  - Route 함수와 Logic 함수 분리
  - Select, Update가 한 함수에서 if로 관리되던 것을 각각의 함수로 분리 (html 수정 포함)

## 2025-01-30 업데이트
1. 리포지토리 브랜치 이름 변경
- 이슈: Github에서 webhook 로그가 정상 (200)으로 보내지고 Jenkins에서 hook log가 출력되는데 파이프라인 트리거가 되질 않음
- 해결: 브랜치 이름이 25-01-28로 되어 있었는데 master로 바꾸고 난 뒤에는 파이프라인 트리거 잘 됨

2. Docker에서 Flask가 실행되지 않음
- 원인 1: DB가 시작되기 전에 Flask를 구동하려고 하면 error 발생
  - 해결: wait.sh 파일을 통해 60초간 DB 상태를 체크해서 Flask를 구동하도록 Dockerfile 반영
- 원인 2: `wait-for-it.sh` 파일이 Linux에서 사용되기 위해 줄바꿈 형식을 LF로 설정할 필요가 있음
  - Github로 push될 때까지만 해도 해당 설정이 유지되는데
  - Jenkins에서 clone하고 image로 빌드하는 과정에서 해당 설정이 CRLF로 변경됨
  - 개발 환경의 Git 설정을 변경해도 해결 안됨 (`git config --global core.autocrlf false`)
  - Github 리포지토리에 LF 설정을 적용하는 `.gitattributes` 파일을 추가해도 해결 안됨
  - 해결: Jenkins 워크스페이스 초기화 후 해결 확인
  - Git config인지, `.gitattributes` 파일 때문인지, 기존 워크스페이스에 있는 파일에 덮어쓰기가 되지 않고 무시돼서 발생한 문제인지 해결 포인트 못 찾음

## 2025-01-29 업데이트
- Docker 환경에서 구동될 수 있도록 config file 추가
  - rest api: `config.ini` (ip, port, path)
  - DB: `mysql.cnf`, `init.sql` (계정 생성)
    - `init.sql`은 추후에 삭제 검토 (root 계정만 사용해서 다른 계정 생성할 필요 없어 보임)
- Docker build 시 필요한 yml 파일 추가
  - DB, server 정보 작성 및 해당 정보로 서버 구동
- Docker에서 실행할 경우 Flask로 구동 중인 web app에 진입 안 되는 이슈 해결
  - 0.0.0.0으로 진입이 되질 않아서 default page에 진입한 ip, port를 이어서 사용하는 코드 추가 (`request.host`)
- Docker에서 `NodeJS` server도 구동되도록 compose file 추가

## 2025-01-28 업데이트
- `Github webhooks` -> `Jenkins pipeline` 연동

## 2025-01-22 업데이트
- `excel_read`, rest api server 이원화
