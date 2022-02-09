#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<vector<int>> a(3, vector<int>(3));
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) cin >> a[i][j];
  }
  int n;
  cin >> n;
  unordered_set<int> called;
  for (int i = 0; i < n; i++) {
    int b;
    cin >> b;
    called.insert(b);
  }
  vector<vector<bool>> flag(3, vector<bool>(3));
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      flag[i][j] = called.find(a[i][j]) != called.end();
    }
  }
  string ans = "No";
  for (int i = 0; i < 3; i++) {
    bool ok = true;
    for (int j = 0; j < 3; j++) {
      if (flag[i][j]) continue;
      ok = false;
      break;
    }
    if (ok) {ans = "Yes"; break;}
  }
  for (int j = 0; j < 3; j++) {
    bool ok = true;
    for (int i = 0; i < 3; i++) {
      if (flag[i][j]) continue;
      ok = false;
      break;
    }
    if (ok) {ans = "Yes"; break;}
  }
  bool ok = true;
  for (int i = 0; i < 3; i++) {
    if (flag[i][i]) continue;
    ok = false;
    break;
  }
  if (ok) ans = "Yes";
  ok = true;
  for (int i = 0; i < 3; i++) {
    if (flag[i][2-i]) continue;
    ok = false;
    break;
  }
  if (ok) ans = "Yes";
  cout << ans << '\n';
  return 0;
}
