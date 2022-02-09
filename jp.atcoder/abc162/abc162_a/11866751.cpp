#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string n;
  cin >> n;
  string ans = "No";
  for (auto &c : n) {
    if (c == '7') {
      ans = "Yes";
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
