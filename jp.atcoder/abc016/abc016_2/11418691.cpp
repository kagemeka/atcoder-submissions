#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c;
  cin >> a >> b >> c;
  bool bl1 = a + b == c;
  bool bl2 = a - b == c;

  char op;
  if (bl1) {
    if (bl2) op = '?';
    else op = '+';
  } else {
    if (bl2) op = '-';
    else op = '!';
  }
  cout << op << '\n';
  return 0;
}
