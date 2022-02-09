#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
  while (b) {
    int c = a % b;
    a = b;
    b = c;
  }
  return abs(a);
}

int lcm(int a, int b) {
  return abs(a / gcd(a, b) * b);
}

int main() {
  int a, b, n;
  cin >> a >> b >> n;
  int l = lcm(a, b);
  int ans = (n + l - 1) / l * l;
  cout << ans << endl;
  return 0;
}
