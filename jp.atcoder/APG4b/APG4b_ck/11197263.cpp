#include <bits/stdc++.h>
using namespace std;

int main() {
  int ans = 1;
  string s;
  cin >> s;
  int n = s.size();
  for (int i = 0; i < n; i++) {
    if (s.at(i) == '+') {
      ans++;
    } else if (s.at(i) == '-') {
      ans--;
    }
  }
  cout << ans << endl;
  return 0;
}
