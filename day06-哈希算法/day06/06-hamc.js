
// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function HMACEncrypt() {
    var text = "1"
    var key = "secret"   // 密钥文件 在客户端和服务器各保留一份  前端肯定可以获取的
    return CryptoJS.HmacSHA1(text, key).toString();
}
console.log(HMACEncrypt())






