const CryptoJS = require('crypto-js')

function hmacS512(val,key){
    return CryptoJS.HmacSHA512(val,key).toString()
}

_xl = {
"n": 20,
"codes": {
    "0": "W",
    "1": "l",
    "2": "k",
    "3": "B",
    "4": "Q",
    "5": "g",
    "6": "f",
    "7": "i",
    "8": "i",
    "9": "r",
    "10": "v",
    "11": "6",
    "12": "A",
    "13": "K",
    "14": "N",
    "15": "k",
    "16": "4",
    "17": "L",
    "18": "1",
    "19": "8"
}
}
var r = function() {
            for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
                var a = t[i].charCodeAt() % _xl.n;
                n += _xl.codes[a]
            }
            return n
        };

var s = function() {
        var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
          , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
          , n = JSON.stringify(e).toLowerCase();
        return hmacS512(t + n, r(t)).toLowerCase().substr(8, 20)
    };

// 获取value
var _s = function() {
            var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
              , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
              , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
              , i = JSON.stringify(e).toLowerCase();
            return hmacS512 (n + "pathString" + i + t,r(n))
        };

// var arg1 = "/api/datalist/touzilist?keyno=5dffb644394922f9073544a08f38be9f&pageindex=1&keyno=5dffb644394922f9073544a08f38be9f&pageindex=1"
// var arg2 = undefined
// console.log(s(arg1,arg2));
//
// var varg1 = "/api/datalist/touzilist?keyno=5dffb644394922f9073544a08f38be9f&pageindex=1&keyno=5dffb644394922f9073544a08f38be9f&pageindex=1"
// var varg2 = undefined
//
// value = _s(varg1,varg2,varg3)
// console.log(value);

function run(url){
    var varg3 = "65fa04a4069e9c2c251843df21787cce"
    key = s(url,undefined)
    value = _s(url,undefined,varg3)
    var headers = {}
    return headers[key] = value,
        headers
}

console.log(run("/api/datalist/touzilist?keyno=5dffb644394922f9073544a08f38be9f&pageindex=2"));



