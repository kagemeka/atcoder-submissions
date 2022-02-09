#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string a, b;
  cin >> a >> b;
  int n = stoi(a + b);
  string ans = (n == pow(floor(sqrt(n)), 2)) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
