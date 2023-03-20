var NodeRSA = require('node-rsa');

function rsaEncrypt() {
    pubKey = new NodeRSA(publicKey,'pkcs8-public');
    var encryptedData = pubKey.encrypt(text, 'base64');
    return encryptedData
}

function rsaDecrypt() {
    priKey = new NodeRSA(privatekey,'pkcs8-private');
    var decryptedData = priKey.decrypt(encryptedData, 'utf8');
    return decryptedData
}

var key = new NodeRSA({b: 1024});                    //生成512位秘钥
var publicKey = key.exportKey('pkcs8-public');    //导出公钥
var privatekey = key.exportKey('pkcs8-private');  //导出私钥
var text = "1324asf123"

var encryptedData = rsaEncrypt()
var decryptedData = rsaDecrypt()

console.log("加密字符串: ", encryptedData)
console.log("解密字符串: ", decryptedData)

