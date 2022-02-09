#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  unordered_set<char> exist;
  for (int i = 0; i < n; i++) {
    char c;
    cin >> c;
    exist.insert(c);
  }
  string ans = (exist.size() == 3) ? "Three" : "Four";
  cout << ans << '\n';
  return 0;
}
