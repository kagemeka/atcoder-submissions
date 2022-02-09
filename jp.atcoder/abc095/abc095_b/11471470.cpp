#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, x;
  cin >> n >> x;
  vector<int> m(n);
  for (int i = 0; i < n; i++) {
    cin >> m[i];
  }

  int s = 0;
  int minimum = 1001001;
  for (int &v : m) {
    minimum = min(minimum, v);
    s += v;
  }
  cout << n + (x - s) / minimum << '\n';
  return 0;
}
