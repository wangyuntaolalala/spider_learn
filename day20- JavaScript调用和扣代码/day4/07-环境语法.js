

// 重点学习语法结构  就是执行环境与浏览器的区别
// 什么是补环境 就是让执行的JS 尽量与浏览器一致      北极熊放广东圈养  尽量模拟北极熊生存的环境

// 这里补一个浏览器环境，不用全补了，能跑通对应的逻辑就好了，缺啥补啥
location = {}
location.href = 'https://wangdoc.com/javascript/bom/location#%E5%B1%9E%E6%80%A7'
function  ps(){
    if (location.href.length>1){
        return 'hello world'
    } else {
        return 'xxxx'
    }
}
console.log(ps());
// 补的是代码运行所需要的环境

navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

window = {
    navigator: navigator,
    document:{
        cookie:'_gid=GA1.2.269285598.1676988229; Hm_lvt_5eec262881855af3dede6a71234571f6=1676988229,1677066585; trc_cookie_storage=taboola%2520global%253Auser-id%3D8dfc9116-526f-4a3e-8e9f-8a1e311c7868-tuct9d27a56; _gat_gtag_UA_111269443_1=1; _ga_ETCV30HD2T=GS1.1.1677073306.5.1.1677074131.0.0.0; _ga=GA1.1.4095506.1676988229; Hm_lpvt_5eec262881855af3dede6a71234571f6=1677074132'
    }
}

console.log(window.document.cookie);
console.log(window['document'].cookie);
console.log(navigator.userAgent);
console.log(location.hostname);  // 不存在的 提取 返回 undefined

