#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int ans = ((a + b - 1) / b * b) - a;
  cout << ans << endl;
  return 0;
}
