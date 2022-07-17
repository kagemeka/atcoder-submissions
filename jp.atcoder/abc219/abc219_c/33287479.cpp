#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string t;
  int n;
  cin >> t >> n;
  int const k = 26;
  vector<int> rank(k);
  for(int i = 0; i < k; i++) { rank[t[i] - 'a'] = i; }
  vector<string> s(n);
  for(int i = 0; i < n; i++) { cin >> s[i]; }
  vector<vector<int>> a(n);
  for(int i = 0; i < n; i++) {
    for(auto& c: s[i]) { a[i].push_back(rank[c - 'a']); }
  }
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  sort(idx.begin(), idx.end(), [&](int i, int j) { return a[i] < a[j]; });
  for(auto& i: idx) { cout << s[i] << endl; }
}
