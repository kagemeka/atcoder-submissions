#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;

  vector<string> res;
  int i = 0;
  while (i < s.size()) {
    int j = s.find("+", i);
    res.push_back(s.substr(i, j - i));
    if (j == -1) break;
    i = j + 1;
  }
  int cnt = 0;
  for (auto &t : res) {
    cnt += t.find("0") == -1;
  }
  cout << cnt << '\n';
  return 0;
}
