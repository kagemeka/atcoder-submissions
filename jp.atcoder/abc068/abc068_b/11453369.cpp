#include <bits/stdc++.h>
using namespace std;

long pow(long x, int n) {
  int m = n;
  n = abs(n);
  long long res = 1;
  while (n) {
    if (n & 1) res *= x;
    x *= x;
    n >>= 1;
  }
  long ans =  (m >= 0) ? res : 1.0 / res;
  return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  cout << pow(2, n) << '\n';
  return 0;
}
