#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s;
  cin >> n >> s;
  for (int i = 0; i < s.size(); i++) {
    int ord = s[i] - 'A';
    ord += n;
    ord %= 26;
    s[i] = (char)('A' + ord);
  }
  cout << s << '\n';
  return 0;
}
