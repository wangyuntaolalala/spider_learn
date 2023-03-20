// console.log('hel')

//调用和声明都有即可，顺序不要求
console.log(func1(123, 45, 'asdad', 'adsaas'));  //传入的参数和实际要求的参数个数不一样也没问题，没有传入的位置对应undefined，多出来也不会报错，直接被arguments吃掉了
Func1(123, 'as')
function func1(a, b, d) {
    console.log(123)
    return a, d
}

function Func1() {
    console.log(231)
    console.log(arguments, typeof arguments)  //arguments直接获取参数，以obj的形式保存
}

//但是这种不可以，因为变量提升问题，编一阶段会扫一遍代码，此时对应的sss()???
// sss();
// sss = function (){
//     console.log(123);
// }


//自执行函数
(function () {
  console.log("Hello World!");
})();
//貌似不用像教程里的那样加叹号，但是分号得有
(function () {
  console.log("Hello Worladsad!");
})();

//内部函数外部调用，其实就是借助var的全局变量作用，实现对象的传递
var _xl;  //全局变量在界面关闭后消失，局部变量在函数执行完毕后消失
!(function () {
    function xl(){
        console.log('hello')
    }
    _xl = xl;
})();
_xl()


//json转化
//方便json数据和str的快速转化，

// ss(99,88,77)  //加了var也不行
var ss = function (a,b,c) {
    console.log(a,b,c)
}

//对象
var car = {name: 'Benz', color: 'red'}  //属性名加引号和不加好像都行
console.log(car.name)
//对象中创建方法
var cars = {
    name:'hi',
    color: 'red',
    printName: function()
    {
        console.log(this.name);
    }
}
//通过[]和.访问都是可读可写的
cars['name'] = 'auto'
cars.printName()
driver = new Object();
driver.name = 'wyt'
console.log(driver['name'])
