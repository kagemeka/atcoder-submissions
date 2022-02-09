#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  char op;
  cin >> a >> op >> b;
  int res = (op == '+') ? a + b : a - b;
  cout << res << endl;
  return 0;
}
