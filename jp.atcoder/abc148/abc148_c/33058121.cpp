#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b;
  cin >> a >> b;
  int a0 = a, b0 = b;
  while(b) {
    a %= b;
    swap(a, b);
  }
  cout << (long)a0 / a * b0 << endl;
}
