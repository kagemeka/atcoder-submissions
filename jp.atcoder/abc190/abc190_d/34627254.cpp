#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long s;
  cin >> s;
  s <<= 1;
  int cnt = 0;
  vector<long> divs;
  for(long i = 1; i * i <= s; i++) {
    if(s % i) continue;
    divs.push_back(i);
    if(i * i != s) divs.push_back(s / i);
  }
  for(auto& n: divs) {
    long x = s / n - n + 1;
    if(x & 1) continue;
    cnt++;
  }
  cout << cnt << endl;
}
