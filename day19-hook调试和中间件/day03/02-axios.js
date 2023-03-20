
axios = require('axios')

// 拼接的  =>
// 比如添加头部参数
axios.interceptors.request.use(function (config) {
    console.log('请求拦截器 成功')
    config.timeout = 2000; //修改请求config
    config.headers['sign'] = "exs4CQYVFQ1Udg4WPjl7XgA1Mlk4WlVHUFkISwhXUgQaI0dJTEwCBwFTXVIPAyFBUA=="
    return config;
}, function (error) {
    console.log('请求拦截器 失败')
    return Promise.reject(error);
});

//设置响应拦截器
axios.interceptors.response.use(function (response) {
    console.log('响应拦截器 成功')
    console.log('调解密函数进行解密数据')
    //return response;
    return {'name':'夏洛到此一游'}; //修改响应数据
}, function (error) {
    console.log('响应拦截器 失败')
    return Promise.reject(error);
});


// axios.get('http://httpbin.org/get').then(res=>console.log(res))  箭头函数
axios.get('http://httpbin.org/get').then(function (res){
    console.log(res)
    console.log(res.data)
})



