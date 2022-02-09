#include <bits/stdc++.h>
using namespace std;

int main() {
  string s, t;
  cin >> s >> t;
  string ans = (s.size() > t.size()) ? s : t;
  cout << ans << endl;
  return 0;
}
