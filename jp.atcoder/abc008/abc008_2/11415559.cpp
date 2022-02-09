#include <bits/stdc++.h>
using namespace std;

bool by_value(pair<string, int> &a, pair<string, int> &b) {
  return a.second < b.second;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  map<string, int> res;

  int n;
  cin >> n;
  string s;
  for (int i = 0; i < n; i++) {
    cin >> s;
    res[s]++;
  }

  int m = 0;
  string ans;
  for (auto &x : res) {
    if (x.second > m) {
      ans = x.first;
      m = x.second;
    }
  }
  cout << ans << endl;
  return 0;
}
