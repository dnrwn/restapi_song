# Flask 애플리케이션 설정
FROM python:3.12

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 모듈 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y bash

# wait-for-it.sh 스크립트 복사
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# 코드 복사
COPY . .

# 서버 시작
CMD ["./wait-for-it.sh", "db:3306", "--strict", "--timeout=60", "--", "python", "server/main.py"]
