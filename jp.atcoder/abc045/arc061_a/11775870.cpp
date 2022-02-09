#include <bits/stdc++.h>
using namespace std;

int pow2(int x, int n) {
  if (n == 0) return 1;
  if (n & 1) return x * pow(x, n - 1);
  int h = pow(x, n / 2);
  return h * h;
}

int c(int n) {return pow2(2, max(0, n - 1));}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s;
  cin >> s;
  int n = s.size();
  long long res = 0;
  for (int l = 0; l < n; l++) {
    for (int r = l; r < n; r++) {
      res += stoll(s.substr(l, r - l + 1)) * c(l) * c(n - 1 - r);
    }
  }
  cout << res << '\n';
  return 0;
}
