#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long const k = 1 << 13;
  long const k2 = k * k;
  long cnt = 0;
  for(int i = 1; i < k; i++) {
    for(int j = i; j < k2; j++) {
      if(n / (i * j) < j) break;
      cnt += max(0l, n / (i * j) - j + 1);
    }
  }
  cout << cnt << endl;
}
