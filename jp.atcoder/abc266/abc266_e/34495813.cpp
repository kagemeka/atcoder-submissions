#include <bits/stdc++.h>
using namespace std;
auto f(int n) -> double {
  if(n == 1) return 3.5;
  double e = 0;
  double x = f(n - 1);
  for(int i = 1; i < 7; i++) { e += max<double>(i, x); }
  return e / 6;
}
auto main() -> int {
  int n;
  cin >> n;
  cout << setprecision(16) << f(n) << endl;
}
