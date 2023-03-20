#### 3.5  hook技术

Hook 是一种钩子技术，在系统没有调用函数之前，钩子程序就先得到控制权，这时钩子函数既可以加工处理（改变）该函数的执行行为，也可以强制结束消息的传递。简单来说，**修改原有的 JS 代码就是 Hook**。

**Hook 技术之所以能够实现有两个条件：**

- 客户端拥有 JS 的最高解释权，可以决定在任何时候注入 JS，而服务器无法阻止或干预。服务端只能通过检测和混淆的手段，另 Hook 难度加大，但是无法直接阻止。
- 除了上面的必要条件之外，还有一个条件。就是 JS 是一种弱类型语言，同一个变量可以多次定义、根据需要进行不同的赋值，而这种情况如果在其他强类型语言中则可能会报错，导致代码无法执行。js 的这种特性，为我们 Hook 代码提供了便利。



**注意：**JS 变量是有作用域的，只有当被 hook 函数和 debugger 断点在同一个作用域的时候，才能 hook 成功。

##### 3.5.1 *Hook步骤：*

+ 1 寻找hook的点

+ 2 编写hook逻辑

+ 3 调试

**注**：最常用的是`hook cookie`

#####  3.5.2 hook 方法

站点：https://fanyi.youdao.com/index.html#/

我们知道在 `JavaScript` 中 `JSON.stringify()` 方法用于将` JavaScript` 对象或值转换为 `JSON` 字符串，`JSON.parse()` 方法用于将一个 `JSON `字符串转换为`JavaScript` 对象，某些站点在向` web` 服务器传输用户名密码时，会用到这两个方法

```javascript
// JSON.parse('{name:xxx}')
(function() {
    var _parse = JSON.parse;
    JSON.parse = function(ps) {
        console.log("Hook JSON.parse ——> ", ps);
        debugger;
        return _parse(ps);  // 不改变原有的执行逻辑 
    }
})();
```

首先定义了一个变量 `stringify` 保留原始 `JSON.stringify` 方法，然后重写 `JSON.stringify` 方法，遇到 `JSON.stringify` 方法就会执行 `debugger` 语句，会立即断下，最后将接收到的参数返回给原始的 `JSON.stringify` 方法进行处理，确保数据正常传输

##### 3.5.3 hook  XHR请求

**案例地址：**https://www.qimai.cn

定义了一个变量 `open` 保留原始 `XMLHttpRequest.open` 方法，然后重写 `XMLHttpRequest.open` 方法，判断如果 rnd 字符串值在 URL 里首次出现的位置不为 -1，即 URL 里包含 `analysis`字符串，则执行 `debugger` 语句，会立即断下。

```javascript
// 如果是正数 表示存在里面
// 如果是-1 表示不在里面

(function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("analysis") != -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
})();
```

**Interceptors**-拦截器

+ 请求拦截器：在发送请求之前，可以借助一些函数来对请求的内容和参数做一些检测。若有问题可以直接取消请求。
+ 响应拦截器：当服务器返回响应数据时，响应拦截器会在我们拿到结果前预先处理响应数据。例如对响应数据做一些格式化处理，或者当响应失败时，可以做一些失败提醒和纪录。

```javascript
// npm install axios
axios = require('axios')
//设置请求拦截器
axios.interceptors.request.use(function (config) {
    console.log('请求拦截器 成功')
    config.timeout = 2000; //修改请求config
    config.headers['sign'] = 'lili'
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
    return response.data; //修改响应数据
}, function (error) {
    console.log('响应拦截器 失败')
    return Promise.reject(error);
});

//发送请求
axios.get('http://httpbin.org/get').then(res=>console.log(res))
```

**XMLHttpRequest**

`XMLHttpRequest`（XHR）对象用于与服务器交互。通过 XMLHttpRequest 可以在不刷新页面的情况下请求特定 URL，获取数据。这允许网页在不影响用户操作的情况下，更新页面的局部内容。`XMLHttpRequest` 在 [AJAX](https://developer.mozilla.org/zh-CN/docs/Glossary/AJAX) 编程中被大量使用。

[`XMLHttpRequest.open()`](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/open)

方法初始化一个新创建的请求，或重新初始化一个请求。

```
xhrReq.open(method, url, async);
```

[`XMLHttpRequest.send()`](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/send)

发送请求。如果请求是异步的（默认），那么该方法将在请求发送后立即返回。

方法接受一个可选的参数，其作为请求主体；如果请求方法是 GET 或者 HEAD,则应将请求主体设置为 null。

```
xhrReq.send(body)
```

[`XMLHttpRequest.setRequestHeader()`](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/setRequestHeader)

设置 HTTP 请求头的值。必须在 `open()` 之后、`send()` 之前调用 `setRequestHeader()` 方法。

```javascript
myReq.setRequestHeader(header, value);    // headers['key'] = value
```

[`XMLHttpRequest.onreadystatechange`](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/readystatechange_event)

当 `readyState` 属性发生变化时，调用的事件处理器。

```javascript
var xhr= new XMLHttpRequest(),
    method = "GET",
    url = "https://developer.mozilla.org/";

xhr.open(method, url, true);
xhr.onreadystatechange = function () {
  if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
    console.log(xhr.responseText)
  }
}
xhr.send();
```



##### 3.5.4 HOOK cookie操作

`WEBAPI`地址：https://developer.mozilla.org/zh-CN/docs/Web/API

`Object.defineProperty `为对象的属性赋值，替换对象属性

基本语法：`Object.defineProperty(obj, prop, descriptor)`，它的作用就是直接在一个对象上定义一个新属性，或者修改一个对象的现有属性，接收的三个参数含义如下：

+ `obj`：需要定义属性的当前对象；

+ `prop`：当前需要定义的属性名；

```javascript
Object.defineProperty(user,"age",{
 get:function(){
      console.log("这个人来获取值了！！");
      return count;
 },
    
 set:function(newVal){
      console.log("这个人来设置值了！！");
      count=newVal+1;
 }
})
```

**cookie 示范**

示范例子：http://q.10jqka.com.cn/

cookie 钩子用于定位 cookie 中关键参数生成位置，以下代码演示了当 cookie 中匹配到了 `v`， 则插入断点：

```JavaScript
(function () {
  var cookieTemp = '';
  Object.defineProperty(document, 'cookie', {
    set: function (val) {
      if (val.indexOf('v') != -1) {
        debugger;
      }
      console.log('Hook捕获到cookie设置->', val);
      cookieTemp = val;
      return val;
    },
    get: function () {
      return cookieTemp;
    },
  });
})();
```

注：正常`hook cookie`操作的时候需要清除下`cookie`

