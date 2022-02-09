#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, l;
  cin >> n >> l;
  vector<string> s(n);
  for (int i = 0; i < n; i++) {
    cin >> s[i];
  }
  sort(s.begin(), s.end());
  for (string &t : s) {
    cout << t;
  }
  cout << '\n';
  return 0;
}
