개요 : API를 Postman을 통해 메뉴얼로 테스트할 경우 결과를 자동으로 수집해주는 기능이 필요하여 작성하였음
- 메뉴얼로 테스트 후 Response를 각각 수집할 수 있으나 한 가지 동작 (Step)이라도 줄이는 등으로 효율을 높히기 위함

로직 : postman_response_node.pptx
1. Postman -> API Server = Request Call
2. API Server -> Postman = Response Return
3. Postman -> Node JS Server = Data 전달
4. Node JS Server = 전달 받은 Data 가공
5. Node JS Server = 가공된 Data 저장

자료1. Postman > Test 에 작성
- postman_test_script.js

자료2. Node js 로 실행
- postman_response_node_v1.4.0.js
