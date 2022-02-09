#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  vector<int> a(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> a[i];
  for (int i = 0; i < n; i++) a[i+1] += a[i];
  long long s = 0;
  for (int i = 0; i < n - k + 1; i++) {
    s += a[i+k] - a[i];
  }
  cout << s << '\n';
  return 0;

}
