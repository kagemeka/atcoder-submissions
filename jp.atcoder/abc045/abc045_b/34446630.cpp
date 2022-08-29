#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  vector<string> a(3);
  for(int i = 0; i < 3; i++) cin >> a[i];
  int t = 0;
  for(int i = 0; i < 3; i++) reverse(a[i].begin(), a[i].end());
  while(a[t].size()) {
    int i = a[t].back() - 'a';
    a[t].pop_back();
    t = i;
  }
  cout << (char)('A' + t) << endl;
}
