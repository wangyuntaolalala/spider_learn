## JavaScript逆向基础

#### 学习收获

+ 爬虫对抗的参数加密
+ JavaScript基本语法
+ JavaScript作用域
+ JavaScript函数编写



学习前必备基础能力

+ 有python编程、爬虫基本功底、、JavaScript语法知识

学习需要的工具

```
chrome node.js  pycharm 
```

学习周期

+ 接近2个月  5月更新安卓

学完能做啥

+ 达到就业、兼职技术、可以独立解决 极验、瑞数、其他JS签名、jsv6
[Scikit-learn00.ipynb](..%2F..%2F..%2Fprograms%2F%B8%F7%C0%E0%CE%C4%B5%B5%2Fcollege%2F%BF%F2%BC%DC%2FScikit-learn00.ipynb)


### 1 逆向声明[Scikit-learn00.ipynb](..%2F..%2F..%2Fprograms%2F%B8%F7%C0%E0%CE%C4%B5%B5%2Fcollege%2F%BF%F2%BC%DC%2FScikit-learn00.ipynb)

#### 1.1 为什么要学逆向

+ 头部签名验证
  + https://ygp.gdzwfw.gov.cn/#/44/jygg
+ 请求参数签名验证
  + https://www.jizhy.com/44/rank/school
+ cookie验证
  + https://www.mafengwo.cn/i/5376978.html
+ 响应数据验证
  + https://ggzyfw.fj.gov.cn/business/list/



### 2.  JavaScript 是脚本语言

+ JavaScript 是一种轻量级的编程语言。

+ JavaScript 是可插入 HTML 页面的编程代码。

+ JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。

+ JavaScript 很容易学习



### 3. 如何在Pycharm里面运行JS

任何的编程语言想要执行都需要有一个好的环境，python如此、JavaScript也是如此。

#### 3.1 node

```
Node.js 是一个基于 Chrome V8 引擎的 JavaScript 运行
```

**下载：**http://nodejs.cn/download/



### 4. JavaScript语法

#### 4.1 注释

```
单行注释以 // 开头
多行注释以 /* 开始，以 */ 结尾
```



#### 4.2 变量和数据类型

**一、var 的使用以及作用域**

(1).作用域是指函数或变量的可供访问的范围。

(2). var可以定义全局变量和局部变量

(3). var的作用域主要和函数的定义有关

​			I.全局作用域

​				如果是在任意函数的外部声明var变量，其作用域是全局的；

​			II.局部（函数）作用域

​				如果是在函数内部声明var，其作用域是局部的，只能在函数内部被访问；

​				对其他块定义没有作用域，比如if、for,这就会导致外部同名变量可以随意修改在if/for内定义的变量。

​			III. var 的声明与变量提升

​				在使用变量前，需要先对变量进行声明，如果只声明、未赋值，则会初始化值为undefined。

​				var可以修改，也可以被重复声明。当对var 进行重复声明时，后面的变量可以覆盖前面的变量，相当于变量重置。

​				var的变量提升： JS引擎在预编译代码时，会优先获取所有被var声明的变量和函数，将它们放在代码的头部然后从上到下执行。

与代数一样，JavaScript 变量可用于存放值（比如 x=5）和表达式（比如 z=x+y）。

JavaScript 变量有很多种类型，但是现在，我们只关注数字和字符串

```javascript
var pi=3.14;  
// 如果你熟悉 ES6，pi
// const pi = 3.14;
var person="John Doe";
var answer='Yes I am!';
```

##### 4.2.1 声明（创建） JavaScript 变量

我们使用 var 关键词来声明变量：

```javascript
// 先声明 再赋值
var carname;
carname="Volvo";
// 声明变量时对其赋值
var carname="Volvo";
```

##### 4.2.2 一条语句，多个变量

可以在一条语句中声明很多变量。该语句以 var 开头，并使用逗号分隔变量即可：

```
var lastname="Doe", age=30, job="carpenter";
```

##### 二、 let 的使用以及作用域

`ES2015(ES6)` 新增加了两个重要的 `JavaScript `关键字: **let** 和 **const**。

+ `let` 声明的变量只在` let` 命令所在的代码块内有效。


**注意：**var是函数[作用域](https://so.csdn.net/so/search?q=作用域&spm=1001.2101.3001.7020)，let是块作用域。块作用域由 { } 包括；

​    (1).let允许声明一个作用域被限制在 块级中的变量、语句或者表达式。与 var 关键字不同的是， var声明的变量只能是全局或者整个函数块的。

​	(2).let声明的变量 只在它所处的代码块内有效，属于块级作用域。块是由 { } 界定的。

​	(3).let 可以被修改，但不能被重复声明。 

​	(4).let不存在变量提升

​	(5).暂存性死区

1、let不能被重新定义，但是var是可以的

```JavaScript

let dogs = "狗"
let dogs = "猫"
console.log(dogs)

var dog = "狗"
var dog = "猫"
console.log(dog)
```

2、***声明的变量具有块作用域（局部变量）的特征***

在这之中定义的所有变量在代码块外都是不可见的，我们称之为块级作用域。

```javascript
let xa = 2
{
    let xa = 3
    console.log(xa)
}
```

`var`声明的变量存在变量提升（将变量提升到当前作用域的顶部）。即变量可以在声明之前调用，值为`undefined`。
`let`和`const`不存在变量提升。即它们所声明的变量一定要在声明后使用，否则报`ReferenceError`错

**三、 const 的使用以及作用域**

​	(1). 像let声明一样，`const` 声明只能在声明它们的块级作用域中访问

​	(2). `const` 声明一个只读的常量，这意味着声明后的常量不能被修改并且不能被重复声明,这也意味着const声明时就必须初始化，不能等到之后赋值。

​			**所以，当我们修饰的标识符不会被再次赋值时, 就可以使用const来保证数据的安全性。**



**四、总结**

​	作用域：

​		var声明的是全局作用域或函数作用域；而let和 const 是块作用域。

​	声明初始化：

​		var和let在声明的时候可以不进行初始化；而 const 在声明的时候必须初始化。

​	修改与重复声明：

​		var在可以修改和重复声明；而let只能修改，不能在同一作用域下重复声明；const 声明常量不可修改也不可重复声明。

​	变量提升：

​		var声明的变量存在变量提升，即变量可以在声明之前调用，值为undefined；let和 const 不存在变量提升，即它们所声明的变量一定要在声明后使用，否则会报错。

​	暂存性死区：

​		var不存在暂时性死区；let和const存在暂存性死区，只有等到声明变量的那一行代码出现，才可以获取和使用该变量。



#### 5. JavaScript 函数语法

函数就是包裹在花括号中的代码块，前面使用了关键词 function：

```javascript
function functionname()
{
    // 执行代码
}
```

**注：** JavaScript 对大小写敏感。关键词 function 必须是小写的，并且必须以与函数名称相同的大小写来调用函数。

##### 5.1 有名函数

```javascript
function xxs(){
    console.log('123')
}
xxs();
```

##### 5.2 函数赋值表达式定义函数

```javascript
sss = function (a,b,c){
    console.log(b)
}
sss(1)
```

##### 5.3 JavaScript之自执行函数

一种理解是，自执行即自动执行，也就是所谓的立即执行函数

```javascript
!(function () {
  console.log("Hello World!");
})();
```

在前面加上一个布尔运算符（只多了一个感叹号），就是表达式了，将执行后面的代码

##### 5.4 内部函数外部调用

```javascript
var _xl;
!(function () {
    function xl(){
        console.log('hello')
    }
    _xl = xl;
})();
_xl()
```



#### 6. 作用域

变量在函数内声明，变量为局部变量，具有局部作用域。

局部变量：只能在函数内部访问

变量在函数外定义，即为全局变量。

```javascript
as = 123
function xxss(){
    console.log(as)
    var ddd = 10;
}
console.log(as)
```



##### 6.1 JavaScript 变量生命周期

+ JavaScript 变量生命周期在它声明时初始化。
+ 局部变量在函数执行完毕后销毁。
+ 全局变量在页面关闭后销毁。



#### 7. 对象

JavaScript中的对象其实就是一组数据和功能的集合。

通过new操作符后跟要创建的对象类型的名称来创建。

对象也是一个变量，但对象可以包含多个值（多个变量），每个值以 **name:value** 对呈现。

```javascript
var car = {name:"xialuo", model:500, color:"white"};
```

创建了对象的一个新实例

```javascript
person = new Object();
```

这里的Object相当于祖宗一样，创建Object的实例并没有什么用处。

特点：

每个Object类型的实例共有的属性和方法：

- constructor： 保存着用于创建当前对象的函数。
- hasOwnProperty：用于检测给定的属性在当前对象的实例中是否存在。
- isPrototypeOf ： 用于检查传入的对象是否是当前对象的原型
- propertyIsEnumerble ： 用于检查给定属性能否使用for-in来枚举
- toLocaleString() : 返回对象的字符串表示。
- toString() : 返回对象的字符串表示。
- valueOf() : 返回对象的字符串，数值，或布尔表示。通常和toString() 返回的值相同。 

```javascript
person.firstname="John";
person.lastname="Doe";
person.age=50;
```

##### 7.1 对象访问

```javascript
person.firstname;
person['firstname']
```

##### 7.2 对象方法

对象的方法定义了一个函数，并作为对象的属性存储。

 ```javascript
var person = {
    firstName: "xl",
    lastName : "lili",
    id : 5566,
    fullName : function()
	{
       return this.firstName + " " + this.lastName;
    }
};
 ```

**注:**在对象方法中， `this` 指向调用它所在方法的对象。



#### 8 JavaScript事件

HTML 事件是发生在 HTML 元素上的事情。

当在 HTML 页面中使用 JavaScript 时， JavaScript 可以触发这些事件。

##### 8.1 登陆举例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<input type="text" id="name">
<input type="text" id="pwd">
<button onclick="xl()">登陆</button>

<script>
    function xl(){
         var name = document.getElementById("name").value
         var pwd = document.getElementById("pwd").value
        console.log(name,pwd)
    }
</script>

</body>
</html>
```

#### 9 json转换

```javascript
JSON.parse()	    // 用于将一个 JSON 字符串转换为 JavaScript 对象。
JSON.stringify()	// 用于将 JavaScript 值转换为 JSON 字符串。
```

注：经常使用在数据的处理方面，比如后台返回数据。所以后台返回的加密数据，可以使用分析`JSON.parse` 来找加密位置   体现在请求后

注：`JSON.stringify` 用在数据加密后，变成字符串传给后台服务器    		体现在请求前

##### 实例演示

```javascript
// 要实现从JSON字符串转换为JS对象，使用 JSON.parse() 方法
var obj = JSON.parse('{"a": "Hello", "b": "World"}')
// 要实现从JS对象转换为JSON字符串，使用 JSON.stringify() 方法：
var json = JSON.stringify({a: 'Hello', b: 'World'});
```



10 作业

+ 已练习为主、把今天讲的内容  自己写一次

