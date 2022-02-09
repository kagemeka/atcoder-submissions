#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  int n = s.size();
  int k;
  cin >> k;
  unordered_set<string> res;
  for (int i = 0; i < n - k + 1; i++) {res.insert(s.substr(i, k));}
  cout << res.size() << '\n';
  return 0;
}
