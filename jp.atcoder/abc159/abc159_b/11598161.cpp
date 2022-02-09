#include <bits/stdc++.h>
using namespace std;

bool is_palindrome(string s) {
  int n = s.size() / 2;
  string t, w;
  t = s.substr(0, n);
  reverse(s.begin(), s.end());
  w = s.substr(0, n);
  return t == w;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  string ans = (is_palindrome(s) && is_palindrome(s.substr(0, s.size() / 2))) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
