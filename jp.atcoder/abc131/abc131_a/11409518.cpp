#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  string ans = "Good";
  for (int i = 0; i < 3; i++) {
    if (s[i] == s[i+1]) {
      ans = "Bad";
      break;
    }
  }
  cout << ans << endl;
  return 0;
}
