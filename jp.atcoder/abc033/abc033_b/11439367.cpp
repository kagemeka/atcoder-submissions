#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  map<string, int> res;
  int tot = 0;
  string s;
  int p;
  for (int i = 0; i < n; i++) {
    cin >> s >> p;
    res[s] = p;
    tot += p;
  }
  double half = tot / 2.0;
  string ans = "atcoder";
  for (auto &sp : res) {
    if (sp.second > half) {
      ans = sp.first;
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
