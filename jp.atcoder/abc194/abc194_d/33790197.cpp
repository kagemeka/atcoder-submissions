#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  function<double(int)> f;
  f = [&](int c) -> double {
    if(c == n) return 0;
    double p = (double)(n - c) / n;
    return (f(c + 1) * p + 1) / p;
  };
  cout << setprecision(16) << f(1) << endl;
}
