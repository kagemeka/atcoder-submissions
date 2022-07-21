#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  string perm = "ABC";
  vector<int> id(3 * n, -1);
  int k = 0;
  do {
    int cnt = n;
    for(int i = 0; i < 3; i++) {
      int c = 0;
      for(int j = i * n; j < (i + 1) * n; j++) { c += s[j] == perm[i]; }
      cnt = min(cnt, c);
    }
    if(cnt == 0) continue;
    k++;
    for(int i = 0; i < 3; i++) {
      int c = 0;
      for(int j = i * n; j < (i + 1) * n; j++) {
        if(c == cnt) break;
        if(s[j] != perm[i] || id[j] != -1) continue;
        id[j] = k;
        c++;
      }
    }
  } while(next_permutation(perm.begin(), perm.end()));
  for(auto& i: id) {
    assert(1 <= i && i <= 6);
    cout << i;
  }
  cout << endl;
}
