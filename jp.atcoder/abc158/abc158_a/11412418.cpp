#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  unordered_set<char> a;
  char c;
  for (int i = 0; i < 3; i++) {
    cin >> c;
    a.insert(c);
  }

  string ans = (a.size() == 1) ? "No" : "Yes";
  cout << ans << endl;
  return 0;
}
