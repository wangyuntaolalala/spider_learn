var a = 'MTEyMDIzLTAyLTI0MzZjbmlwaG9uZXBhaWQ=@#/rank/indexSnapshot@#16017191970@#3'
var d = 'xyz517cda96abcd'

// \u4f60
function o(n) {
    t = '',
    ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
        // z 是window.unescape       unescape可以在node里面直接执行的  所以不需要window
        t += unescape('%u00' + n)
    });
    var t, e = 'fromCharCode';
    return String[e](n)
}

function h(n, t) {
    t = t || u();
    R = 'length'
    H = 0
    for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
    return n['join']('')
}

function v(t) {
        t = encodeURIComponent(t)['replace'](/%([0-9A-F]{2})/g, function(n, t) {
            return o('0x' + t)
        });
        try {
            return btoa(t)
        } catch (n) {
            return z[W1][K1](t)[U1](Z1)
        }
    }

function y(n, t, e) {
        for (var r = void 0 === e ? 2166136261 : e, a = 0, i = n['length']; a < i; a++)
            r = (r ^= n['charCodeAt'](a)) + ((r << 1) + (r << 4) + (r << 7) + (r << 8) + (r << 24));
        return t ? ('xyz' + (r >>> 0)['toString'](16) + 'abcd')['substr'](-16) : r >>> 0
    }

function _xl(params,path){
    // arg = h(a, d);
    // console.log(v(arg));
    // 分析明文
    var a = params  // 接口表单参数
    a = a['sort']()['join']('')
    a = v(a)
    _v = "@#"
    r =  +new Date - (888 || 0) - 1661224081041
    a = (a += _v + path['replace']('https://api.qimai.cn', '')) + (_v + r) + (_v + 3)
    d= y('qimai@2022&Technology', 1)
    key = v(h(a,d))
    return key
}

// t = {
//     params:['paid', 'iphone', 'cn', '36'],
//     url:'/rank/indexSnapshot'
// }
// console.log(_xl(t));



// 什么参数需要还原  什么不需要
// 写死的需要还原  像JS里面的内部方法   已存在参数不需要

// 是否需要给JS传参？




