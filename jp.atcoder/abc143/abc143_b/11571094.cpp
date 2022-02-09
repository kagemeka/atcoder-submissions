#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> d(n);
  for (int i = 0; i < n; i++) cin >> d[i];
  vector<int> s = d;
  for (int i = 0; i < n - 1; i++) {
    s[i+1] += s[i];
  }
  int tot = 0;
  for (int i = 0; i < n - 1; i++) {
    tot += d[i] * (s[n-1] - s[i]);
  }
  cout << tot << '\n';
  return 0;
}
