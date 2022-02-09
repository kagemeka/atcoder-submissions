#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;

  s += '$';
  string t = "";
  int cnt = 0;
  char prev = s[0];
  for (char &c : s) {
    if (c == prev) cnt++;
    else {
      t += prev + to_string(cnt);
      cnt = 1;
      prev = c;
    }
  }
  cout << t << '\n';
  return 0;
}
