#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int const k = 3;
  vector<int> a(k + 1);
  for(int i = 0; i < k + 1; i++) {
    char c;
    cin >> c;
    a[i] = c - '0';
  }
  for(int s = 0; s < 1 << k; s++) {
    int res = a[0];
    string t = "";
    t += '0' + a[0];
    for(int i = 0; i < k; i++) {
      int x = a[i + 1];
      if(s >> i & 1) {
        res += x;
        t += "+";
      } else {
        t += "-";
        res -= x;
      }
      t += '0' + x;
    }
    t += "=7";
    if(res == 7) {
      cout << t << endl;
      return 0;
    }
  }
}
