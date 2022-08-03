#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  double s = 0;
  for(int i = 0; i < n; i++) {
    double x;
    string u;
    cin >> x >> u;
    if(u == "JPY") {
      s += x;
    } else {
      s += x * 380000.0;
    }
  }
  cout << setprecision(16) << s << endl;
}
