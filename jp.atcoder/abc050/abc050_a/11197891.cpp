#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  char op;
  cin >> a;
  cin >> op;
  cin >> b;
  int ans = (op == '+') ? a + b : a - b;
  cout << ans << endl;
  return 0;
}
