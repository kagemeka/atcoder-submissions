#include <bits/stdc++.h>
using namespace std;

int main() {
  int m, d;
  cin >> m >> d;
  string ans = (m % d == 0) ? "YES" : "NO";
  cout << ans << endl;
  return 0;
}
