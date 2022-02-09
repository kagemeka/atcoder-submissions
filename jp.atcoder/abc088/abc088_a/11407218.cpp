#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, a;
  cin >> n >> a;
  a %= 500;
  string ans = (a <= n) ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
