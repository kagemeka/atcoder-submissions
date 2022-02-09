#include <bits/stdc++.h>
using namespace std;


void solve() {
  string s = "123456";
  int n;
  cin >> n;
  n %= 30;
  for (int i = 0; i < n; i++) {
    swap(s[i%5], s[i%5 + 1]);
  }
  cout << s << '\n';
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    solve();
  }

  return 0;
}
