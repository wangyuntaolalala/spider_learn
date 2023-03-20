// function  == def

function xl(){
    // 里面是代码块
    console.log('123')
}

function Xl(a,b,c,d){
    // 暂存性死区
    // console.log(xx)
    // let xx = 5
    // 里面是代码块
    console.log(234)
    // 默认参数
    console.log(arguments,typeof arguments)
    // JS 参数可以不传值 结果是undefined
    console.log(a,b,d)
    return a  // 终止了
    e = 5
    console.log(e)
}
console.log(Xl({'name':'夏洛'}, '456', '123','asd','asdasd'));
// 遵循key value形式


sss = function (a){
    console.log('123')
}
sss(1);




// 自执行函数
!(function (){}())

(function (){
    // 代码块
    console.log(234)
})()

// 在前面添加修饰符  !推荐使用

var xx = 2 //全局
var _xl;
!(function (){
    // 代码块
    console.log(123)
    // 内部方法
    function _x(){
        return 'abc'
    }
    // 局部变量
    var xx = 1
    _xl = _x  // 加括号和不加的区别 一个是方法体本身 一个是调用后的  导出 引用内部的方法
})()












