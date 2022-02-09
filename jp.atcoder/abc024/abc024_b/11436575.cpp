#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, t;
  cin >> n >> t;
  int tot = 0;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int start = a[0];
  for (int &s : a) {
    tot += min(s - start, t);
    start = s;
  }
  tot += t;
  cout << tot << '\n';
  return 0;
}
