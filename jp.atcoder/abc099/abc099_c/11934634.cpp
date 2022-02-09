#include <bits/stdc++.h>
using namespace std;

int count(int n, int b) {
  int res = 0;
  while (n) {
    res += n % b;
    n /= b;
  }
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  int res = 1001001001;
  for (int i = 0; i < n + 1; i++) {
    res = min(res, count(i, 6) + count(n - i, 9));
  }
  cout << res << '\n';
  return 0;

}
