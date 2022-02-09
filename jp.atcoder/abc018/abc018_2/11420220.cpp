#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int n;
  cin >> n;
  int l, r;
  for (int i = 0; i < n; i++) {
    cin >> l >> r;
    l--; r--;
    reverse(s.begin()+l, s.begin()+r+1);
  }
  cout << s << '\n';
  return 0;
}
