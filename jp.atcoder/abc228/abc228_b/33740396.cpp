#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, x;
  cin >> n >> x;
  x--;
  vector<int> a(n);
  for(int i = 0; i < n; i++) {
    cin >> a[i];
    a[i]--;
  }
  vector<int> known(n);
  int cnt = 0;
  while(true) {
    known[x] = true;
    cnt++;
    if(known[a[x]]) break;
    x = a[x];
  }
  cout << cnt << endl;
}
