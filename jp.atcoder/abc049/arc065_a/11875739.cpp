#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  vector<string> t = {"dream", "dreamer", "erase", "eraser"};
  int l = s.size();
  while (!s.empty()) {
    bool flag = false;
    for (string &x : t) {
      if (s.size() < x.size()) continue;
      if (s.substr(s.size()-x.size(), x.size()) == x) {
        s.erase(s.size()-x.size(), x.size());
        flag = true;
      }
    }
    if (!flag) {
      cout << "NO" << '\n';
      return 0;
    }
  }
  cout << "YES" << '\n';
  return 0;
}
