#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> l(n);
  for (int i = 0; i < n; i++) {
    cin >> l[i];
  }
  sort(l.begin(), l.end());
  int s = accumulate(l.begin(), l.end(), 0);
  string ans = (l[n-1] < (s + 1) / 2) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
