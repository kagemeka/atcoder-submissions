
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  long n;
  cin >> n;
  int cnt = 0;
  for(int i = 1; i < 1 << 20; i++) {
    string s = to_string(i);
    long x = stol(s + s);
    cnt += x <= n;
  }
  cout << cnt << endl;
}
