#include <bits/stdc++.h>

using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int mod = (int)1e9 + 7;
  string s; cin >> s;
  string t = "$chokudai";
  map<char, int> ind;
  for (
    int i = 0;
    i < (int)t.size();
    i++
  ) {
    ind[t[i]] = i;
  }
  map<char, int> cnt;
  cnt['$'] = 1;
  for (char x: s) {
    if (!ind.count(x))
      continue;
    cnt[x] += cnt[t[ind[x]-1]];
    cnt[x] %= mod;
  }
  cout << cnt['i'] << '\n';

}
