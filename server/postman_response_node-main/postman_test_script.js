let response = pm.response.json(); // response 변수
response.case_name = pm.info.requestName; //send 시 Case Name 전달

pm.sendRequest
(
    {
        url: 'http://localhost:3000/launches', // 파일이 저장될 Server IP
        method: 'POST',
        header: {
            'Content-Type': 'application/JSON'
        }, 
        body: {
            mode: 'raw',
            raw: response
        }
    },
    function (err, res) {
        console.log(res)
    }
)
