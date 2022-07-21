#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  n = (n + 1) * n >> 1;
  if(n < 2) {
    cout << "BOWWOW" << endl;
    return 0;
  }
  for(int i = 2; i * i <= n; i++) {
    if(n % i == 0) {
      cout << "BOWWOW" << endl;
      return 0;
    }
  }
  cout << "WANWAN" << endl;
}
