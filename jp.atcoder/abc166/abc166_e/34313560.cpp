#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  map<int, int> cnt;
  long res = 0;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    res += cnt[i - x];
    cnt[x + i]++;
  }
  cout << res << endl;
}
