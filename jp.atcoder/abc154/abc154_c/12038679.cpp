#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  unordered_set<int> res;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    res.insert(a);
  }
  string ans = (res.size() == n) ? "YES" : "NO";
  cout << ans << '\n';
  return 0;
}
