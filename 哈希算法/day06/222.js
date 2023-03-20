s = function() {
                var e = function(e, t) {
                    var r;
                    if ("undefined" !== typeof window && window.crypto && (r = window.crypto),
                    "undefined" !== typeof self && self.crypto && (r = self.crypto),
                    "undefined" !== typeof globalThis && globalThis.crypto && (r = globalThis.crypto),
                    !r && "undefined" !== typeof window && window.msCrypto && (r = window.msCrypto),
                    !r && "undefined" !== typeof i && i.crypto && (r = i.crypto),
                    !r)
                        try {
                            r = n(2)
                        } catch (g) {}
                    var a = function() {
                        if (r) {
                            if ("function" === typeof r.getRandomValues)
                                try {
                                    return r.getRandomValues(new Uint32Array(1))[0]
                                } catch (g) {}
                            if ("function" === typeof r.randomBytes)
                                try {
                                    return r.randomBytes(4).readInt32LE()
                                } catch (g) {}
                        }
                        throw new Error("Native crypto module could not be used to get secure random number.")
                    }
                      , o = Object.create || function() {
                        function e() {}
                        return function(t) {
                            var n;
                            return e.prototype = t,
                            n = new e,
                            e.prototype = null,
                            n
                        }
                    }()
                      , s = {}
                      , l = s.lib = {}
                      , u = l.Base = function() {
                        return {
                            extend: function(e) {
                                var t = o(this);
                                return e && t.mixIn(e),
                                t.hasOwnProperty("init") && this.init !== t.init || (t.init = function() {
                                    t.$super.init.apply(this, arguments)
                                }
                                ),
                                t.init.prototype = t,
                                t.$super = this,
                                t
                            },
                            create: function() {
                                var e = this.extend();
                                return e.init.apply(e, arguments),
                                e
                            },
                            init: function() {},
                            mixIn: function(e) {
                                for (var t in e)
                                    e.hasOwnProperty(t) && (this[t] = e[t]);
                                e.hasOwnProperty("toString") && (this.toString = e.toString)
                            },
                            clone: function() {
                                return this.init.prototype.extend(this)
                            }
                        }
                    }()
                      , c = l.WordArray = u.extend({
                        init: function(e, n) {
                            e = this.words = e || [],
                            this.sigBytes = n != t ? n : 4 * e.length
                        },
                        toString: function(e) {
                            return (e || h).stringify(this)
                        },
                        concat: function(e) {
                            var t = this.words
                              , n = e.words
                              , i = this.sigBytes
                              , r = e.sigBytes;
                            if (this.clamp(),
                            i % 4)
                                for (var a = 0; a < r; a++) {
                                    var o = n[a >>> 2] >>> 24 - a % 4 * 8 & 255;
                                    t[i + a >>> 2] |= o << 24 - (i + a) % 4 * 8
                                }
                            else
                                for (var s = 0; s < r; s += 4)
                                    t[i + s >>> 2] = n[s >>> 2];
                            return this.sigBytes += r,
                            this
                        },
                        clamp: function() {
                            var t = this.words
                              , n = this.sigBytes;
                            t[n >>> 2] &= 4294967295 << 32 - n % 4 * 8,
                            t.length = e.ceil(n / 4)
                        },
                        clone: function() {
                            var e = u.clone.call(this);
                            return e.words = this.words.slice(0),
                            e
                        },
                        random: function(e) {
                            for (var t = [], n = 0; n < e; n += 4)
                                t.push(a());
                            return new c.init(t,e)
                        }
                    })
                      , d = s.enc = {}
                      , h = d.Hex = {
                        stringify: function(e) {
                            for (var t = e.words, n = e.sigBytes, i = [], r = 0; r < n; r++) {
                                var a = t[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                                i.push((a >>> 4).toString(16)),
                                i.push((15 & a).toString(16))
                            }
                            return i.join("")
                        },
                        parse: function(e) {
                            for (var t = e.length, n = [], i = 0; i < t; i += 2)
                                n[i >>> 3] |= parseInt(e.substr(i, 2), 16) << 24 - i % 8 * 4;
                            return new c.init(n,t / 2)
                        }
                    }
                      , f = d.Latin1 = {
                        stringify: function(e) {
                            for (var t = e.words, n = e.sigBytes, i = [], r = 0; r < n; r++) {
                                var a = t[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                                i.push(String.fromCharCode(a))
                            }
                            return i.join("")
                        },
                        parse: function(e) {
                            for (var t = e.length, n = [], i = 0; i < t; i++)
                                n[i >>> 2] |= (255 & e.charCodeAt(i)) << 24 - i % 4 * 8;
                            return new c.init(n,t)
                        }
                    }
                      , p = d.Utf8 = {
                        stringify: function(e) {
                            try {
                                return decodeURIComponent(escape(f.stringify(e)))
                            } catch (t) {
                                throw new Error("Malformed UTF-8 data")
                            }
                        },
                        parse: function(e) {
                            return f.parse(unescape(encodeURIComponent(e)))
                        }
                    }
                      , m = l.BufferedBlockAlgorithm = u.extend({
                        reset: function() {
                            this._data = new c.init,
                            this._nDataBytes = 0
                        },
                        _append: function(e) {
                            "string" == typeof e && (e = p.parse(e)),
                            this._data.concat(e),
                            this._nDataBytes += e.sigBytes
                        },
                        _process: function(t) {
                            var n, i = this._data, r = i.words, a = i.sigBytes, o = this.blockSize, s = 4 * o, l = a / s;
                            l = t ? e.ceil(l) : e.max((0 | l) - this._minBufferSize, 0);
                            var u = l * o
                              , d = e.min(4 * u, a);
                            if (u) {
                                for (var h = 0; h < u; h += o)
                                    this._doProcessBlock(r, h);
                                n = r.splice(0, u),
                                i.sigBytes -= d
                            }
                            return new c.init(n,d)
                        },
                        clone: function() {
                            var e = u.clone.call(this);
                            return e._data = this._data.clone(),
                            e
                        },
                        _minBufferSize: 0
                    })
                      , v = (l.Hasher = m.extend({
                        cfg: u.extend(),
                        init: function(e) {
                            this.cfg = this.cfg.extend(e),
                            this.reset()
                        },
                        reset: function() {
                            m.reset.call(this),
                            this._doReset()
                        },
                        update: function(e) {
                            return this._append(e),
                            this._process(),
                            this
                        },
                        finalize: function(e) {
                            e && this._append(e);
                            var t = this._doFinalize();
                            return t
                        },
                        blockSize: 16,
                        _createHelper: function(e) {
                            return function(t, n) {
                                return new e.init(n).finalize(t)
                            }
                        },
                        _createHmacHelper: function(e) {
                            return function(t, n) {
                                return new v.HMAC.init(e,n).finalize(t)
                            }
                        }
                    }),
                    s.algo = {});
                    return s
                }(Math);
                 return function(t) {
                    var n = e
                      , i = n.lib
                      , r = i.WordArray
                      , a = i.Hasher
                      , o = n.algo
                      , s = []
                      , l = [];
                    (function() {
                        function e(e) {
                            for (var n = t.sqrt(e), i = 2; i <= n; i++)
                                if (!(e % i))
                                    return !1;
                            return !0
                        }
                        function n(e) {
                            return 4294967296 * (e - (0 | e)) | 0
                        }
                        var i = 2
                          , r = 0;
                        while (r < 64)
                            e(i) && (r < 8 && (s[r] = n(t.pow(i, .5))),
                            l[r] = n(t.pow(i, 1 / 3)),
                            r++),
                            i++
                    }
                    )();
                    var u = []
                      , c = o.SHA256 = a.extend({
                        _doReset: function() {
                            this._hash = new r.init(s.slice(0))
                        },
                        _doProcessBlock: function(e, t) {
                            for (var n = this._hash.words, i = n[0], r = n[1], a = n[2], o = n[3], s = n[4], c = n[5], d = n[6], h = n[7], f = 0; f < 64; f++) {
                                if (f < 16)
                                    u[f] = 0 | e[t + f];
                                else {
                                    var p = u[f - 15]
                                      , m = (p << 25 | p >>> 7) ^ (p << 14 | p >>> 18) ^ p >>> 3
                                      , v = u[f - 2]
                                      , g = (v << 15 | v >>> 17) ^ (v << 13 | v >>> 19) ^ v >>> 10;
                                    u[f] = m + u[f - 7] + g + u[f - 16]
                                }
                                var _ = s & c ^ ~s & d
                                  , y = i & r ^ i & a ^ r & a
                                  , b = (i << 30 | i >>> 2) ^ (i << 19 | i >>> 13) ^ (i << 10 | i >>> 22)
                                  , w = (s << 26 | s >>> 6) ^ (s << 21 | s >>> 11) ^ (s << 7 | s >>> 25)
                                  , k = h + w + _ + l[f] + u[f]
                                  , x = b + y;
                                h = d,
                                d = c,
                                c = s,
                                s = o + k | 0,
                                o = a,
                                a = r,
                                r = i,
                                i = k + x | 0
                            }
                            n[0] = n[0] + i | 0,
                            n[1] = n[1] + r | 0,
                            n[2] = n[2] + a | 0,
                            n[3] = n[3] + o | 0,
                            n[4] = n[4] + s | 0,
                            n[5] = n[5] + c | 0,
                            n[6] = n[6] + d | 0,
                            n[7] = n[7] + h | 0
                        },
                        _doFinalize: function() {
                            var e = this._data
                              , n = e.words
                              , i = 8 * this._nDataBytes
                              , r = 8 * e.sigBytes;
                            return n[r >>> 5] |= 128 << 24 - r % 32,
                            n[14 + (r + 64 >>> 9 << 4)] = t.floor(i / 4294967296),
                            n[15 + (r + 64 >>> 9 << 4)] = i,
                            e.sigBytes = 4 * n.length,
                            this._process(),
                            this._hash
                        },
                        clone: function() {
                            var e = a.clone.call(this);
                            return e._hash = this._hash.clone(),
                            e
                        }
                    });
                    n.SHA256 = a._createHelper(c),
                    n.HmacSHA256 = a._createHmacHelper(c)
                }(Math),
                e
            }
console.log(s());

console.log(s().SHA256("/open/noauth/search-pc?api_key=51job&timestamp=1677497710&keyword=python&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=2&requestId=084bd9d4ee8e3681e62a6e0c5085ce21&pageSize=50&source=1&accountId=&pageCode=sou%7Csou%7Csoulb").toString());
