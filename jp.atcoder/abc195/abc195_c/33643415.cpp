#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long p = 1;
  long cnt = 0;
  for(int i = 1; i <= 15; i++) {
    p *= 10;
    if(i % 3) continue;
    cnt += max(0l, n - p + 1);
  }
  cout << cnt << endl;
}
