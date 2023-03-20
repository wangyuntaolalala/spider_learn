_xls = (function() {
    var t =t || function(t, e) {
                    var n = Object.create || function() {
                        function t() {}
                        return function(e) {
                            var n;
                            return t.prototype = e,
                            n = new t,
                            t.prototype = null,
                            n
                        }
                    }()
                      , r = {}
                      , i = r.lib = {}
                      , o = i.Base = {
                        extend: function(t) {
                            var e = n(this);
                            return t && e.mixIn(t),
                            e.hasOwnProperty("init") && this.init !== e.init || (e.init = function() {
                                e.$super.init.apply(this, arguments)
                            }
                            ),
                            e.init.prototype = e,
                            e.$super = this,
                            e
                        },
                        create: function() {
                            var t = this.extend();
                            return t.init.apply(t, arguments),
                            t
                        },
                        init: function() {},
                        mixIn: function(t) {
                            for (var e in t)
                                t.hasOwnProperty(e) && (this[e] = t[e]);
                            t.hasOwnProperty("toString") && (this.toString = t.toString)
                        },
                        clone: function() {
                            return this.init.prototype.extend(this)
                        }
                    }
                      , a = i.WordArray = o.extend({
                        init: function(t, n) {
                            t = this.words = t || [],
                            this.sigBytes = n != e ? n : 4 * t.length
                        },
                        toString: function(t) {
                            return (t || s).stringify(this)
                        },
                        concat: function(t) {
                            var e = this.words
                              , n = t.words
                              , r = this.sigBytes
                              , i = t.sigBytes;
                            if (this.clamp(),
                            r % 4)
                                for (var o = 0; o < i; o++) {
                                    var a = n[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                                    e[r + o >>> 2] |= a << 24 - (r + o) % 4 * 8
                                }
                            else
                                for (o = 0; o < i; o += 4)
                                    e[r + o >>> 2] = n[o >>> 2];
                            return this.sigBytes += i,
                            this
                        },
                        clamp: function() {
                            var e = this.words
                              , n = this.sigBytes;
                            e[n >>> 2] &= 4294967295 << 32 - n % 4 * 8,
                            e.length = t.ceil(n / 4)
                        },
                        clone: function() {
                            var t = o.clone.call(this);
                            return t.words = this.words.slice(0),
                            t
                        },
                        random: function(e) {
                            for (var n, r = [], i = function(e) {
                                var n = 987654321
                                  , r = 4294967295;
                                return function() {
                                    var i = ((n = 36969 * (65535 & n) + (n >> 16) & r) << 16) + (e = 18e3 * (65535 & e) + (e >> 16) & r) & r;
                                    return i /= 4294967296,
                                    (i += .5) * (t.random() > .5 ? 1 : -1)
                                }
                            }, o = 0; o < e; o += 4) {
                                var c = i(4294967296 * (n || t.random()));
                                n = 987654071 * c(),
                                r.push(4294967296 * c() | 0)
                            }
                            return new a.init(r,e)
                        }
                    })
                      , c = r.enc = {}
                      , s = c.Hex = {
                        stringify: function(t) {
                            for (var e = t.words, n = t.sigBytes, r = [], i = 0; i < n; i++) {
                                var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                                r.push((o >>> 4).toString(16)),
                                r.push((15 & o).toString(16))
                            }
                            return r.join("")
                        },
                        parse: function(t) {
                            for (var e = t.length, n = [], r = 0; r < e; r += 2)
                                n[r >>> 3] |= parseInt(t.substr(r, 2), 16) << 24 - r % 8 * 4;
                            return new a.init(n,e / 2)
                        }
                    }
                      , u = c.Latin1 = {
                        stringify: function(t) {
                            for (var e = t.words, n = t.sigBytes, r = [], i = 0; i < n; i++) {
                                var o = e[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                                r.push(String.fromCharCode(o))
                            }
                            return r.join("")
                        },
                        parse: function(t) {
                            for (var e = t.length, n = [], r = 0; r < e; r++)
                                n[r >>> 2] |= (255 & t.charCodeAt(r)) << 24 - r % 4 * 8;
                            return new a.init(n,e)
                        }
                    }
                      , l = c.Utf8 = {
                        stringify: function(t) {
                            try {
                                return decodeURIComponent(escape(u.stringify(t)))
                            } catch (t) {
                                throw new Error("Malformed UTF-8 data")
                            }
                        },
                        parse: function(t) {
                            return u.parse(unescape(encodeURIComponent(t)))
                        }
                    }
                      , f = i.BufferedBlockAlgorithm = o.extend({
                        reset: function() {
                            this._data = new a.init,
                            this._nDataBytes = 0
                        },
                        _append: function(t) {
                            "string" == typeof t && (t = l.parse(t)),
                            this._data.concat(t),
                            this._nDataBytes += t.sigBytes
                        },
                        _process: function(e) {
                            var n = this._data
                              , r = n.words
                              , i = n.sigBytes
                              , o = this.blockSize
                              , c = i / (4 * o)
                              , s = (c = e ? t.ceil(c) : t.max((0 | c) - this._minBufferSize, 0)) * o
                              , u = t.min(4 * s, i);
                            if (s) {
                                for (var l = 0; l < s; l += o)
                                    this._doProcessBlock(r, l);
                                var f = r.splice(0, s);
                                n.sigBytes -= u
                            }
                            return new a.init(f,u)
                        },
                        clone: function() {
                            var t = o.clone.call(this);
                            return t._data = this._data.clone(),
                            t
                        },
                        _minBufferSize: 0
                    })
                      , h = (i.Hasher = f.extend({
                        cfg: o.extend(),
                        init: function(t) {
                            this.cfg = this.cfg.extend(t),
                            this.reset()
                        },
                        reset: function() {
                            f.reset.call(this),
                            this._doReset()
                        },
                        update: function(t) {
                            return this._append(t),
                            this._process(),
                            this
                        },
                        finalize: function(t) {
                            return t && this._append(t),
                            this._doFinalize()
                        },
                        blockSize: 16,
                        _createHelper: function(t) {
                            return function(e, n) {
                                return new t.init(n).finalize(e)
                            }
                        },
                        _createHmacHelper: function(t) {
                            return function(e, n) {
                                return new h.HMAC.init(t,n).finalize(e)
                            }
                        }
                    }),
                    r.algo = {});
                    return r
                }(Math);
     return function(e) {
                    var n = t
                      , r = n.lib
                      , i = r.Base
                      , o = r.WordArray
                      , a = n.x64 = {};
                    a.Word = i.extend({
                        init: function(t, e) {
                            this.high = t,
                            this.low = e
                        }
                    }),
                    a.WordArray = i.extend({
                        init: function(t, n) {
                            t = this.words = t || [],
                            this.sigBytes = n != e ? n : 8 * t.length
                        },
                        toX32: function() {
                            for (var t = this.words, e = t.length, n = [], r = 0; r < e; r++) {
                                var i = t[r];
                                n.push(i.high),
                                n.push(i.low)
                            }
                            return o.create(n, this.sigBytes)
                        },
                        clone: function() {
                            for (var t = i.clone.call(this), e = t.words = this.words.slice(0), n = e.length, r = 0; r < n; r++)
                                e[r] = e[r].clone();
                            return t
                        }
                    })
                }(),
           function() {
                    var _t = t
                      , n = _t.lib
                      , i = n.Hasher
                      , r = _t.x64
                      , a = r.Word
                      , o = r.WordArray
                      , s = _t.algo;
                    function l() {
                        return a.create.apply(a, arguments)
                    }
                    var u = [l(1116352408, 3609767458), l(1899447441, 602891725), l(3049323471, 3964484399), l(3921009573, 2173295548), l(961987163, 4081628472), l(1508970993, 3053834265), l(2453635748, 2937671579), l(2870763221, 3664609560), l(3624381080, 2734883394), l(310598401, 1164996542), l(607225278, 1323610764), l(1426881987, 3590304994), l(1925078388, 4068182383), l(2162078206, 991336113), l(2614888103, 633803317), l(3248222580, 3479774868), l(3835390401, 2666613458), l(4022224774, 944711139), l(264347078, 2341262773), l(604807628, 2007800933), l(770255983, 1495990901), l(1249150122, 1856431235), l(1555081692, 3175218132), l(1996064986, 2198950837), l(2554220882, 3999719339), l(2821834349, 766784016), l(2952996808, 2566594879), l(3210313671, 3203337956), l(3336571891, 1034457026), l(3584528711, 2466948901), l(113926993, 3758326383), l(338241895, 168717936), l(666307205, 1188179964), l(773529912, 1546045734), l(1294757372, 1522805485), l(1396182291, 2643833823), l(1695183700, 2343527390), l(1986661051, 1014477480), l(2177026350, 1206759142), l(2456956037, 344077627), l(2730485921, 1290863460), l(2820302411, 3158454273), l(3259730800, 3505952657), l(3345764771, 106217008), l(3516065817, 3606008344), l(3600352804, 1432725776), l(4094571909, 1467031594), l(275423344, 851169720), l(430227734, 3100823752), l(506948616, 1363258195), l(659060556, 3750685593), l(883997877, 3785050280), l(958139571, 3318307427), l(1322822218, 3812723403), l(1537002063, 2003034995), l(1747873779, 3602036899), l(1955562222, 1575990012), l(2024104815, 1125592928), l(2227730452, 2716904306), l(2361852424, 442776044), l(2428436474, 593698344), l(2756734187, 3733110249), l(3204031479, 2999351573), l(3329325298, 3815920427), l(3391569614, 3928383900), l(3515267271, 566280711), l(3940187606, 3454069534), l(4118630271, 4000239992), l(116418474, 1914138554), l(174292421, 2731055270), l(289380356, 3203993006), l(460393269, 320620315), l(685471733, 587496836), l(852142971, 1086792851), l(1017036298, 365543100), l(1126000580, 2618297676), l(1288033470, 3409855158), l(1501505948, 4234509866), l(1607167915, 987167468), l(1816402316, 1246189591)]
                      , c = [];
                    (function() {
                        for (var e = 0; e < 80; e++)
                            c[e] = l()
                    }
                    )();
                    var d = s.SHA512 = i.extend({
                        _doReset: function() {
                            this._hash = new o.init([new a.init(1779033703,4089235720), new a.init(3144134277,2227873595), new a.init(1013904242,4271175723), new a.init(2773480762,1595750129), new a.init(1359893119,2917565137), new a.init(2600822924,725511199), new a.init(528734635,4215389547), new a.init(1541459225,327033209)])
                        },
                        _doProcessBlock: function(e, t) {
                            for (var n = this._hash.words, i = n[0], r = n[1], a = n[2], o = n[3], s = n[4], l = n[5], d = n[6], h = n[7], f = i.high, p = i.low, m = r.high, v = r.low, g = a.high, _ = a.low, y = o.high, b = o.low, w = s.high, k = s.low, x = l.high, S = l.low, M = d.high, C = d.low, L = h.high, D = h.low, T = f, O = p, E = m, j = v, Y = g, P = _, $ = y, A = b, I = w, N = k, H = x, F = S, B = M, R = C, z = L, V = D, W = 0; W < 80; W++) {
                                var U, q, G = c[W];
                                if (W < 16)
                                    q = G.high = 0 | e[t + 2 * W],
                                    U = G.low = 0 | e[t + 2 * W + 1];
                                else {
                                    var K = c[W - 15]
                                      , J = K.high
                                      , X = K.low
                                      , Z = (J >>> 1 | X << 31) ^ (J >>> 8 | X << 24) ^ J >>> 7
                                      , Q = (X >>> 1 | J << 31) ^ (X >>> 8 | J << 24) ^ (X >>> 7 | J << 25)
                                      , ee = c[W - 2]
                                      , te = ee.high
                                      , ne = ee.low
                                      , ie = (te >>> 19 | ne << 13) ^ (te << 3 | ne >>> 29) ^ te >>> 6
                                      , re = (ne >>> 19 | te << 13) ^ (ne << 3 | te >>> 29) ^ (ne >>> 6 | te << 26)
                                      , ae = c[W - 7]
                                      , oe = ae.high
                                      , se = ae.low
                                      , le = c[W - 16]
                                      , ue = le.high
                                      , ce = le.low;
                                    U = Q + se,
                                    q = Z + oe + (U >>> 0 < Q >>> 0 ? 1 : 0),
                                    U += re,
                                    q = q + ie + (U >>> 0 < re >>> 0 ? 1 : 0),
                                    U += ce,
                                    q = q + ue + (U >>> 0 < ce >>> 0 ? 1 : 0),
                                    G.high = q,
                                    G.low = U
                                }
                                var de = I & H ^ ~I & B
                                  , he = N & F ^ ~N & R
                                  , fe = T & E ^ T & Y ^ E & Y
                                  , pe = O & j ^ O & P ^ j & P
                                  , me = (T >>> 28 | O << 4) ^ (T << 30 | O >>> 2) ^ (T << 25 | O >>> 7)
                                  , ve = (O >>> 28 | T << 4) ^ (O << 30 | T >>> 2) ^ (O << 25 | T >>> 7)
                                  , ge = (I >>> 14 | N << 18) ^ (I >>> 18 | N << 14) ^ (I << 23 | N >>> 9)
                                  , _e = (N >>> 14 | I << 18) ^ (N >>> 18 | I << 14) ^ (N << 23 | I >>> 9)
                                  , ye = u[W]
                                  , be = ye.high
                                  , we = ye.low
                                  , ke = V + _e
                                  , xe = z + ge + (ke >>> 0 < V >>> 0 ? 1 : 0)
                                  , Se = (ke = ke + he,
                                xe = xe + de + (ke >>> 0 < he >>> 0 ? 1 : 0),
                                ke = ke + we,
                                xe = xe + be + (ke >>> 0 < we >>> 0 ? 1 : 0),
                                ke = ke + U,
                                xe = xe + q + (ke >>> 0 < U >>> 0 ? 1 : 0),
                                ve + pe)
                                  , Me = me + fe + (Se >>> 0 < ve >>> 0 ? 1 : 0);
                                z = B,
                                V = R,
                                B = H,
                                R = F,
                                H = I,
                                F = N,
                                N = A + ke | 0,
                                I = $ + xe + (N >>> 0 < A >>> 0 ? 1 : 0) | 0,
                                $ = Y,
                                A = P,
                                Y = E,
                                P = j,
                                E = T,
                                j = O,
                                O = ke + Se | 0,
                                T = xe + Me + (O >>> 0 < ke >>> 0 ? 1 : 0) | 0
                            }
                            p = i.low = p + O,
                            i.high = f + T + (p >>> 0 < O >>> 0 ? 1 : 0),
                            v = r.low = v + j,
                            r.high = m + E + (v >>> 0 < j >>> 0 ? 1 : 0),
                            _ = a.low = _ + P,
                            a.high = g + Y + (_ >>> 0 < P >>> 0 ? 1 : 0),
                            b = o.low = b + A,
                            o.high = y + $ + (b >>> 0 < A >>> 0 ? 1 : 0),
                            k = s.low = k + N,
                            s.high = w + I + (k >>> 0 < N >>> 0 ? 1 : 0),
                            S = l.low = S + F,
                            l.high = x + H + (S >>> 0 < F >>> 0 ? 1 : 0),
                            C = d.low = C + R,
                            d.high = M + B + (C >>> 0 < R >>> 0 ? 1 : 0),
                            D = h.low = D + V,
                            h.high = L + z + (D >>> 0 < V >>> 0 ? 1 : 0)
                        },
                        _doFinalize: function() {
                            var e = this._data
                              , t = e.words
                              , n = 8 * this._nDataBytes
                              , i = 8 * e.sigBytes;
                            t[i >>> 5] |= 128 << 24 - i % 32,
                            t[30 + (i + 128 >>> 10 << 5)] = Math.floor(n / 4294967296),
                            t[31 + (i + 128 >>> 10 << 5)] = n,
                            e.sigBytes = 4 * t.length,
                            this._process();
                            var r = this._hash.toX32();
                            return r
                        },
                        clone: function() {
                            var e = i.clone.call(this);
                            return e._hash = this._hash.clone(),
                            e
                        },
                        blockSize: 32
                    });
                    t.SHA512 = i._createHelper(d),
                    t.HmacSHA512 = i._createHmacHelper(d)
                }(),
         t
})


console.log(_xls());


