#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  unordered_set<int> ok = {4, 7, 8, 11, 12, 14, 15, 16};
  string ans = (n >= 18 || ok.find(n) != ok.end()) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
