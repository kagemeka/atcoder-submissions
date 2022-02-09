#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> c(26);
  vector<int> cand = {'M'-'A', 0, 'R'-'A', 2, 'H'-'A'};
  for (int i = 0; i < n; i++) {
    string s; cin >> s;
    c[s[0]-'A']++;
  }
  long long res = 0;
  for (int i = 0; i < 3; i++) {
    for (int j = i + 1; j < 4; j++) {
      for (int k = j + 1; k < 5; k++) {
        res += (long long)c[cand[i]] * c[cand[j]] * c[cand[k]];
      }
    }
  }
  cout << res << '\n';
  return 0;
}
