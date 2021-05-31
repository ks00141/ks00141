const axios = require('axios');

axios.get('http://gw.wisol.co.kr/ekp/login.do?cmd=goLogin')
    .then((res)=>{
        console.log(res);
    })