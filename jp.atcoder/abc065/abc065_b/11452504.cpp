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

  unordered_set<int> pressed;
  int now = 0;
  int ans = -1;
  for (int i = 0; i < n; i++) {
    if (pressed.find(now) != pressed.end()) break;
    if (now == 1) {ans = i; break;}
    pressed.insert(now);
    now = a[now];
  }
  cout << ans << '\n';
  return 0;
}
