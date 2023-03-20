

var user = {}
user.name = '莹莹'
// console.log(user)

// 要定义属性的对象。    要定义或修改的属性的名称    要定义或修改的属性描述符
Object.defineProperty(user, 'name', {
    value: 'jy'
})
// console.log(user)


var age = 18
Object.defineProperty(user,'count',{
    get:function (){
        // debugger;   #对于很多加密的东西的获取，很多都用到了debugger进行截断操作，
        return age
    },
    // 在JS里面 JS加密 md5('123123')   document.cookie = md5('123123')
    set :function (val){
        debugger;
        age = val + 1
    }
})
console.log(user.count)
user.count = 30
console.log(user.count)


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


  function xl(){
     return 'hello world'
}

