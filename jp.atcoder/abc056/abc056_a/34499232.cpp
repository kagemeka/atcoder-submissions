#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a[2];
  for(int& i: a) {
    char x;
    cin >> x;
    i = x == 'H';
  }
  cout << (a[0] ^ a[1] ? 'D' : 'H') << endl;
}
