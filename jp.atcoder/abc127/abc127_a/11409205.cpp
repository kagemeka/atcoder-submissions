#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  int c;
  if (a >= 13) {
    c = b;
  } else if (a >= 6) {
    c = b / 2;
  } else {
    c = 0;
  }
  cout << c << endl;
  return 0;
}
