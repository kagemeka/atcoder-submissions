#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<int> neg, pos;
  int zero = 0;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    if(x == 0) {
      zero++;
    } else if(x < 0) {
      neg.push_back(x);
    } else {
      pos.push_back(x);
    }
  }
  int cn = neg.size();
  int cp = pos.size();
  long const mod = 1000000007;
  int c = cp + cn / 2 * 2;
  if((c >= k) && ((k & 1) == 0 || cp & 1)) {
    // positive possible
    sort(neg.begin(), neg.end());
    sort(pos.rbegin(), pos.rend());
    long p = 1;
    int i = 0, j = 0;
    if(k & 1) {
      p *= pos[j];
      p %= mod;
      j++;
      k--;
    }
    while(k >= 2) {
      long x = i < cn - 1 ? (long)neg[i] * neg[i + 1] : 0;
      long y = j < cp - 1 ? (long)pos[j] * pos[j + 1] : 0;
      if(x == 0 && y == 0) break;
      if(x >= y) {
        p *= x % mod;
        i += 2;
      } else {
        j += 2;
        p *= y % mod;
      }
      p %= mod;
      k -= 2;
    }
    while(k) {
      p *= pos[j];
      p %= mod;
      j++;
      k--;
    }
    cout << p << endl;
  } else if(zero) {
    // zero possible
    cout << 0 << endl;
  } else {
    // only negative
    // abs greedy
    vector<int> a;
    for(auto& x: neg) a.push_back(x);
    for(auto& x: pos) a.push_back(x);
    sort(a.begin(), a.end(), [&](int x, int y) { return abs(x) < abs(y); });
    long p = 1;
    for(int i = 0; i < k; i++) {
      p *= a[i];
      p %= mod;
    }
    cout << (p + mod) % mod << endl;
  }
}
