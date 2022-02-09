#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  int k;
  cin >> s >> k;
  set<string> cand;
  for (int j = 1; j <= k; j++) {
    for (int i = 0; i < s.size() - j + 1; i++) {
      cand.insert(s.substr(i, j));
    }
  }
  vector<string> res(cand.begin(), cand.end());
  cout << res[k-1] << '\n';
  return 0;
}
