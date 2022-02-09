'use strict';
const fs = require('fs');
const mod = BigInt(1e9+7);


class ABC041 {
  static A(input) {
    var s, i
    input = input.trim().split('\n');
    [s, i] = input;
    i = parseInt(i, 10);
    console.log(s[i-1]);
  }
  static B(input) {
    var a, b, c;
    input = input.trim().split(' ').map(BigInt);
    [a, b, c] = input;
    var ans = a * b % mod * c % mod;
    ans = Number(ans);
    console.log(ans);
  }
  static C(input) {
    var [n, height] = input.trim().split('\n');
    height = height.split(' ').map(n => parseInt(n, 10));
    n = parseInt(n, 10);
    var height = Object.keys(height).map(key => [parseInt(key, 10)+1, height[key]]);
    height.sort(function(first, second) {
      return (second[1] - first[1]);
    });
    for (var [i, _] of height) {console.log(i);}
  }
  static D(input) {
    var lines = input.trim().split('\n');
    var [n, m] = lines[0].split(' ').map(x => +x);
    var edges = new Array(n).fill(0);
    for (var i = 0; i < m; i++) {
      var [x, y] = lines[1+i].split(' ').map(x => +x);
      edges[x-1] |= 1<<(y-1);
    }
    var comb = new Array(1<<n).fill(null); comb[0] = 1;
    function count(edges, bit) {
      if (comb[bit] != null) {return comb[bit];}
      for (var i = 0; i < n; i++) {
        if (bit>>i&1 && !edges[i]) {
          var nxt_bit = bit & ~(1<<i);
          var nxt_edges = edges.slice();
          for (var j = 0; j < n; j++) {
            nxt_edges[j] &= ~(1<<i);
          }
          comb[bit] += count(nxt_edges, nxt_bit);
        }
      }
      return comb[bit];
    }
    console.log(count(edges, (1<<n)-1));
  }
}


var input = fs.readFileSync('/dev/stdin', 'utf8');
ABC041.D(input);
