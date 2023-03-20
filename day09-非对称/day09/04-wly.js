const JSEncrypt = require('jsencrypt')
const CryptoJS = require('crypto-js')

function get_psd(arg1,arg2,pwd)
{
    var encrypt = new JSEncrypt();
    encrypt.setPublicKey(arg1);
    var encrypted = encrypt.encrypt(arg2 + CryptoJS.SHA512(pwd).toString());
    return encrypted
}









