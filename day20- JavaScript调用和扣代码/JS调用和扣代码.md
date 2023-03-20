#### 3.6 python执行JS的方式

##### 3.6.1 PyExecJS

地址;https://github.com/doloopwhile/PyExecJS

PyExecJS 是使用最多的一种方式，底层实现方式是：在本地 JS 环境下运行 JS 代码

```python
pip install PyExecJS  -i  https://pypi.tuna.tsinghua.edu.cn/simple/
```

3.6.2 读取JS代码

```python
with open(file_name, 'r', encoding='UTF-8') as file:
	result = file.read()
```

3.6.3 execjs 类的compile()方法编译加载上面的 JS 字符串，返回一个上下文对象

```python
context1 = execjs.compile("这里面是JS代码")
```

3.6.4 调用上下文对象的call() 方法执行 JS 方法

```python
result1 = context1.call("函数", "参数1", "参数2")
```

需要注意的，由于 PyExecJS 运行在本地 JS 环境下，使用之前会启动 JS 环境，最终导致运行速度会偏慢

3.6.5 eval执行

eval() 函数计算 JavaScript 字符串，并把它作为脚本代码来执行。

```javascript
print(execjs.eval('Date.now()'))
```

##### 3.6.2  开放接口

官方给出的概念：Express 是基于 Node.js 平台，快速、开放、极简的 Web 开发框架。

通俗的理解：Express 的作用和 Node.js 内置的 http 模块类似，是专门用来创建 Web 服务器的。

Express 的本质：就是一个 npm 上的第三方包，提供了快速创建 Web 服务器的便捷方法。

Express 的中文官网：http://www.expressjs.com.cn/

http 内置模块与 Express 类似于浏览器中 Web API 和 jQuery 的关系。后者是基于前者进一步封装出来的。

7.2.1 安装express

在项目所处的目录中，运行如下的终端命令，即可将 express 安装到项目中使用：

```
npm install express -S
```

7.2.2 创建基本的 Web 服务器

```javascript
// 1.导入 express
const express = require('express');
 
// 2.创建 web 服务器
const app = express();
 
// 3.启动 web 服务器
app.listen(8080, () => {
    console.log('express server running at http://127.0.0.1');
})
```



```javascript
app.get('/user', (req, res) => {
    // 调用express提供的res.send()方法，向客户端响应一个JSON对象
    res.send({name: 'zs', age: 20, gender: '男'})
})
```

监听客户端的GET请求、并向客户端响应具体的内容。本次监听的地址是user，req是请求对象(包含了于请求相关的属性与方法); res为响应对象(包含了与响应相关的属性与方法

7.2.4 获取 URL 中携带的查询参数

```javascript
app.get('/', (req, res) => {
//    通过req.query 可以获取到客户端发送过来的 查询参数
//    注意： 默认情况下，req.query 是一个空对象
    console.log(req.query)
    res.send(req.query)
})
```

7.2.5 获取 URL 中的动态参数

通过req.params对象，可以访问到URL中，通过：匹配到的动态参数：

```javascript
//注意：这里的:id是一个动态的参数
app.get('/user/:id/:name', (req, res) => {
//    req.paraams 是动态匹配到的URL参数，默认也是一个空对象
    console.log(req.params)
    res.send(req.params)
})
```

#### 3.7 浏览器环境补充方法

https://wangdoc.com/javascript/bom/

```javascript
document = {
    cookie:'uuid_tt_dd=10_29360271920-1658044222535-945484; __gads=ID=5b925b796ab29466-22740a5938d50041:T=1658044224:RT=1658044224:S=ALNI_MYZZ3qnATdjgh4YHRlZaBk3TnwTFw; p_uid=U010000',
    location : {
        href:'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=87135040_oem_dg&wd=eval%20JS%20&fenlei=256&oq=eval&rsv_pq=e1b3f2520003297e&rsv_t=7e58%2ByqRgVEysyNAVRctyGmKUct9An%2B6da7wzdVJDXgo7qaAS1DKyn86mLazGA1IqBPpY359&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_btype=t&inputT=860&rsv_sug3=56&rsv_sug1=35&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1037'
    }
}

navigator = {userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

window = {
    document : document,
    navigator:navigator
}
console.log(document.location.href);
document.getElementsByTagName = function(){};
```



#### 3.8 JS调试的基本技巧

1、根据关键词搜索大法   （尽量符合可能在JS里面出现的形式 sign =   sign:  "sign"）

2、使用Hook技术进行拦截  （对象、属性、xhr、cookie等）

3、根据启动调用栈去找关系 (尽量分析 加密可能出现的位置)



3.9 作业

```
地址：https://wangdoc.com/javascript/bom/engine
1、dom结构 里面对象和属性  各写5个
2、bom结构 里面对象和属性  各写5个
重点是:docuemnt  location  navigator  window

交付：提供截图上传
```





