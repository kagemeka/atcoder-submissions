#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
  int c;
  while (b) {
    c = a % b;
    a = b;
    b = c;
  }
  return abs(a);
}

int lcm(int &a, int &b) {
  return abs(a / gcd(a, b) * b);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c;
  cin >> a >> b >> c;

  int l = lcm(a, b);
  string ans = "NO";
  for (int i = a; i <= l; i += a) {
    if (i % b == c) {
      ans = "YES";
      break;
    }
  }
  cout << ans << '\n';
  return 0;

}
