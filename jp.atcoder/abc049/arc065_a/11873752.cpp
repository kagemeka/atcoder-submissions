#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  vector<string> t = {"eraser", "erase", "dreamer", "dream"};
  for (string &t : t) {
    while (true) {
      size_t i = s.find(t);
      if (i == -1) break;
      s.replace(i, i+t.size(), "");
    }
  }
  string ans = (s.empty()) ? "YES" : "NO";
  cout << ans << '\n';
  return 0;
}
