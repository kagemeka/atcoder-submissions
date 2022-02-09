"use strict";
const fs = require('fs');

function product(arr, cand, repeat) {
  var res = [];
  function dfs(arr, cand, repeat) {
    if (arr.length === repeat) {
      res.push(arr);
    } else {
      var nex;
      for (var c of cand) {
        nex = arr.slice(0);
        nex.push(c)
        dfs(nex, cand, repeat);
      }
    }
  }
  dfs(arr, cand, repeat);
  return res;
}

function int(n) {
  return parseInt(n, 10);
}

function main(input) {
  input = input.trim().split('\n');
  var s = input[0];
  var n = int(input[1]);
  var res = product(new Array(), s, 2);
  console.log(res[n-1].join(''));
}

var input = fs.readFileSync('/dev/stdin', 'utf8');
main(input);
