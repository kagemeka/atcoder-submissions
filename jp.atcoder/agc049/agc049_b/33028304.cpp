#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  string s;
  string t;
  cin >> n >> s >> t;

  vector<int> indices;
  for(int i = 0; i < n; i++) {
    if(s[i] == '1') indices.push_back(i);
  }

  int j = 0;

  long cnt = 0;

  for(int i = 0; i < n; i++) {
    if(j < (int)indices.size() && indices[j] == i) j++;
    if(s[i] == t[i]) continue;
    if(j == (int)indices.size()) {
      cout << -1 << endl;
      return 0;
    }
    cnt += indices[j] - i;
    s[indices[j]] = '0';
    j++;
  }
  cout << cnt << endl;
}