# 베이스 이미지 설정
FROM node:20.12.0

# 작업 디렉토리 설정
WORKDIR /app/postman_response_node-main

# package.json 및 package-lock.json 파일 복사
COPY package.json ./

# 종속성 설치
RUN npm install

# 앱 소스 복사
COPY . .

# 애플리케이션 실행 명령어
CMD ["npm", "start"]
