#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s;
  long long k;
  cin >> s >> k;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] != '1') {
      char ans = (k < i + 1) ? '1' : s[i];
      cout << ans << '\n';
      return 0;
    }
  }
}
