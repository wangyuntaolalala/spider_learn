

const express = require('express');

// 2.创建 web 服务器
const app = express();

function enc_pwd(val){
    res = btoa(val)
    return res
}

// 这里的get和fastapi很像
app.get('/user', (req, res) => {
    // 调用express提供的res.send()方法，向客户端响应一个JSON对象
    // res.send({name: 'zs', age: 20, gender: '男'})
    pwd = req.query.name
    _res = enc_pwd(pwd)
    res.send(_res)
})


// 3.启动 web 服务器
app.listen(8080, () => {
    console.log('express server running at http://127.0.0.1');
})



