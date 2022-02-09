#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int res = (a == b) ? a + b : max(a, b) * 2 - 1;
  cout << res << endl;
  return 0;
}
