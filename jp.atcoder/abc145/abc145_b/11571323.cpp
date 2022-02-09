#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s;
  cin >> n >> s;
  string ans = "No";
  if (n % 2 == 0) {
    n /= 2;
    if (s.substr(0, n) == s.substr(n, n)) ans = "Yes";
  }
  cout << ans << '\n';
  return 0;
}
