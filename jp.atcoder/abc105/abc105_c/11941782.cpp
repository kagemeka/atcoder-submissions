#include <bits/stdc++.h>
using namespace std;

string base_convert(long long n, int b) {
  if (!n) return "0";
  string res = "";
  while (n) {
    int r = n % b;
    n /= b;
    if (r < 0) {
      if (b > 0) {r += b, n--;}
      else {r -= b, n++;}
    }
    res += to_string(r);
  }
  reverse(res.begin(), res.end());
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  cout << base_convert(n, -2) << '\n';
  return 0;

}
