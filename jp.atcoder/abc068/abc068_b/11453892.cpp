#include <bits/stdc++.h>
using namespace std;

int pow2(int x, int n) {
  if (n == 0) return 1;
  if (n & 1) return x * pow2(x, n - 1);
  int y = pow2(x, n / 2);
  return y * y;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  cout << pow2(2, floor(log2(n))) << '\n';
  return 0;
}
