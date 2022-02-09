#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  vector<string> t = {"eraser", "erase", "dreamer", "dream"};
  for (int i = 0; i < 4; i++) {
    while (true) {
      size_t j = s.find(t[i]);
      if (j == -1) break;
      s.replace(j, j + t[i].size(), "");
    }
  }
  string ans = (s.empty()) ? "YES" : "NO";
  cout << ans << '\n';
  return 0;
}
