#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    a[i]--;
  }
  int now = 0;
  for (int i = 0; i < n; i++) {
    if (now == 1) {
      cout << i << '\n';
      return 0;
    }
    now = a[now];
  }
  cout << -1 << '\n';
  return 0;
}
