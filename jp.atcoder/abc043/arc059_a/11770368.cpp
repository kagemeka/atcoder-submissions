#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  int s = 0;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    s += a[i];
  }
  int x = round((double)s / n);
  s = 0;
  for (int i = 0; i < n; i++) {
    s += (x - a[i]) * (x - a[i]);
  }
  cout << s << '\n';
  return 0;
}
