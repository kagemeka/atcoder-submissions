#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long s = 0;
  long i = 1;
  while(i <= n) {
    long x = n / i;
    long j = n / x + 1;
    s += x * (j - i);
    i = j;
  }
  cout << s << endl;
}
