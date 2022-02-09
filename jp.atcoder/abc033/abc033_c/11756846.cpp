#include <bits/stdc++.h>
using namespace std;

vector<string> split(string &s, string sep) {
  vector<string> res(0);
  int i = 0;
  while (true) {
    int j = s.find(sep, i);
    res.push_back(s.substr(i, j - i));
    if (j == -1) break;
    i = j + 1;
  }
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s;
  cin >> s;
  int cnt = 0;
  for (auto &t : split(s, "+")) {
    cnt += t.find("0") == -1;
  }
  cout << cnt << '\n';
  return 0;
}
