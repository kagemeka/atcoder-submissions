#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  set<string> used;
  int idx = -1;
  int score = -1;
  for(int i = 0; i < n; i++) {
    string s;
    int t;
    cin >> s >> t;
    if(used.count(s)) continue;
    used.insert(s);
    if(t > score) {
      score = t;
      idx = i;
    }
  }
  cout << idx + 1 << endl;
}