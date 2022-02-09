#include <bits/stdc++.h>
using namespace std;

int pow2(int x, int n) {
  if (n == 0) return 1;
  if (n & 1) return x * pow2(x, n - 1);
  int m = pow2(x, n / 2);
  return m * m;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<int> a(3);
  for (int i = 0; i < 3; i++) {
    cin >> a[i];
  }
  int k;
  cin >> k;
  sort(a.begin(), a.end());
  cout << a[0] + a[1] + a[2] * pow2(2, k) << '\n';
  return 0;
}
