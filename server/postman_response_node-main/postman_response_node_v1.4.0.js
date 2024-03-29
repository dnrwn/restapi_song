/* history
 version 1.4.0 / timestamp로 덮어쓰기 방지, etc Case 수집 x
 작성자 송민규S
 출처 https://www.postman.com/mukeshkbj/workspace/learnpostman/documentation/4454846-4e457c79-a2fd-4192-8966-8421782dd93b	
*/

const execSync = require('child_process').execSync;
const value = process.argv[2]; // 입력을 요구 받는 Parameter 개수 지정

// Response 결과 File 생성을 위한 날짜/시간 생성
function create_date(){
    function pad(n) { return n<10 ? "0"+n : n }
    d=new Date()
    return d.getFullYear() + pad(d.getMonth()+1) + pad(d.getDate())+ "-" + pad(d.getHours()) + pad(d.getMinutes()) + pad(d.getSeconds())
}

// 필수 Module (Server 구동에 필요한 Module) Check
function module_check(){
	try{
		const express = require('express');
		const fs = require('fs');
		const bodyParser = require('body-parser');
		return 1
	}
	catch {
	return 0;
	}
}

// Server Main
function run_server(){
	const express = require('express');
	const fs = require('fs');
	const bodyParser = require('body-parser');
	const app = express();
	app.use(bodyParser.json({
		limit: "50mb" // 파일 크기를 지정하지 않을 경우 원하는 결과가 생성되지 않음. 최대 크기 지정 필요
		})); 
	app.post('/launches', function(req, res){
		if (fs.existsSync(value) == false){ 
			fs.mkdirSync(value); // 디렉토리 조회 디렉토리 생성
		}
		// var date = JSON.stringify(req.header, null, "\t");
		data_c = req.body // 전달받은 data의 body 값만 변수에 저장
		var find_etc = data_c.case_name.indexOf('etc') // Test Case name이 etc일 경우 예외처리 (건너뛰기)
		if (find_etc == -1){ // 
			var outputFilename = value + '//' + data_c.case_name + "-" + create_date(); // 파일 생성 규칙
			console.log(outputFilename); // body 값에 표함되어 있는 Case name 추출
			delete data_c.case_name // Case 구분을 위해 Postman에서 인위적으로 추가한 case_name 값을 변수에서 삭제
			data_d = JSON.stringify(data_c, null, "\t");
		
			fs.writeFileSync(outputFilename + '.json', data_d); // write to the 
			
			res.send('Saved to ' + outputFilename); // Postman console에 file 생성 기록 전달
		}
		else if (find_etc != -1){
			console.log('etc Case 무시');
		}
	});
	var port = 3000;
	app.listen(port);
	console.log('Server가 Postman으로부터 Post를 받게되면 console에 Case Name이 기록됩니다.');
}
if (module_check() == 1){
	if (value == undefined){
		console.log('===========================================');
		console.log('옵션 입력 필요 (옵션 값은 디렉토리 생성에 사용됩니다.)\nServer를 다시 시작해 주세요.\nex) cmd: node [node server file].js -[str]');
		console.log('===========================================');
	}
	else if (value != undefined){
		console.log('Server 시작...');
		run_server();
	}
}
else if (module_check() == 0){
	console.log('===========================================');
	console.log('Server를 실행하기 위해 다음의 모듈이 필요합니다. \n - express\n - body-parser \n - fs \n = npm install express body-parser fs');
	console.log('모듈 설치를 시작합니다.');
	execSync('npm install express body-parser fs').toString();
	console.log('완료... Server를 다시 시작해 주세요.');
	console.log('===========================================');
}
