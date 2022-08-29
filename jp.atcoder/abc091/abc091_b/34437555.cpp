#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  map<string, int> c;
  for(int i = 0; i < n; i++) {
    string s;
    cin >> s;
    c[s]++;
  }
  int m;
  cin >> m;
  for(int i = 0; i < m; i++) {
    string t;
    cin >> t;
    c[t]--;
  }
  int score = 0;
  for(auto& [s, c]: c) { score = max(score, c); }
  cout << score << endl;
}
