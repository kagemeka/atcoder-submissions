#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n);
  for(int i = 0; i < n; i++) { cin >> p[i]; }
  int s = 0;
  int cnt = 0;
  for(int i = 0; i < n; i++) {
    if(p[i] == i + 1) {
      cnt++;
      continue;
    }
    s += cnt / 2 + (cnt & 1);
    cnt = 0;
  }
  s += cnt / 2 + (cnt & 1);
  cout << s << endl;
}
