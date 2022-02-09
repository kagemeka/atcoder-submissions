#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;

  unordered_set<char> appeared;
  string ans = "yes";
  for (char &c : s) {
    if (appeared.find(c) != appeared.end()) {
      ans = "no";
      break;
    }
    appeared.insert(c);
  }
  cout << ans << '\n';
  return 0;

}
