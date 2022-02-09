#include <bits/stdc++.h>
using namespace std;

bool is_palindrome(string s) {
  int n = s.size() / 2;
  string t, w;
  t = s.substr(0, n);
  w = s.substr(n+1, n);
  reverse(w.begin(), w.end());
  return t == w;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int n = s.size() / 2;
  string ans =
    (is_palindrome(s) && is_palindrome(s.substr(0, n))) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
