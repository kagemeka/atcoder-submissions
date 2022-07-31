#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long n;
  cin >> n;
  long s = 0;
  for(long i = 2; i * i <= n; i++) {
    int c = 0;
    while(n % i == 0) {
      c++;
      n /= i;
    }
    for(int j = 1; j <= c; j++) {
      s++;
      c -= j;
    }
  }
  s += n > 1;
  cout << s << endl;
}
