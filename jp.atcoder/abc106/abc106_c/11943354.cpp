#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s;
  long long k;
  int n = min((long long)s.size(), k);
  cin >> s >> k;
  for (int i = 0; i < n; i++) {
    if (s[i] != '1') {
      cout << s[i] << '\n';
      return 0;
    }
  }
  cout << 1 << '\n';
  return 0;
}
