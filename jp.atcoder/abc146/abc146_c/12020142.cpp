#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int a, b;
  long long x;
  cin >> a >> b >> x;
  for (int d = 1; d <= 10; d++) {
    long long y = x - b * d;
    if (y >= a * pow(10, d)) continue;
    cout << y / a << '\n';
    return 0;
  }
  cout << 1000000000 << '\n';
  return 0;
}
