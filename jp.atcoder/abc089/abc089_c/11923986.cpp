#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<char> cand = {'M', 'A', 'R', 'C', 'H'};
  unordered_map<char, int> c;
  for (auto ch : cand) c[ch] = 0;
  for (int i = 0; i < n; i++) {
    string s; cin >> s;
    (c.find(s[0]) != c.end()) ? c[s[0]]++ : c[s[0]] = 1;
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
