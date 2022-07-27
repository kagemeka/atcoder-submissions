#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n, m, d;
  cin >> n >> m >> d;
  long c = d == 0 ? n : (n - d) * 2;
  cout << setprecision(16) << (double)(m - 1) / n * c / n << endl;
}
