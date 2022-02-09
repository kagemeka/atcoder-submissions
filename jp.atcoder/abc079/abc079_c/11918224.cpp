#include <bits/stdc++.h>
using namespace std;



int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<int> a(4);
  for (int i = 0; i < 4; i++) {
    char d;
    cin >> d;
    a[i] = d - '0';
  }
  queue<string> q;
  q.push("");
  vector<char> op = {'+', '-'};
  for (int i = 0; i < 3; i++) {
    int l = q.size();
    for (int j = 0; j < l; j++) {
      auto s = q.front(); q.pop();
      for (auto o : op) {
        q.push(s + o);
      }
    }
  }
  while (!q.empty()) {
    auto s = q.front(); q.pop();
    int tot = a[0];
    string res = to_string(a[0]);
    for (int i = 0; i < 3; i++) {
      if (s[i] == '+') {
        tot += a[i+1];
        res += '+';
      } else {
        tot -= a[i+1];
        res += '-';
      }
      res += to_string(a[i+1]);
    }
    if (tot == 7) {
      cout << res + "=7" << '\n';
      return 0;
    }
  }
}
