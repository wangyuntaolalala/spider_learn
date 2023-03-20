const CryptoJS = require('crypto-js')

function SHA1Encrypt() {
    var text = "1"
    // 用什么算法  改写那一个即可
    return CryptoJS.SHA256(text).toString();
}
console.log(SHA1Encrypt())




