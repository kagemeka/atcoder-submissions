#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  int d;
  if (a == b) {
    d = c;
  } else if (b == c) {
    d = a;
  } else {
    d = b;
  }
  cout << d << endl;
  return 0;
}
