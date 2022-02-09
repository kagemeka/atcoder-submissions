#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  int res = 0;
  for (char c : s) {
    res += (c == '+') ? 1 : -1;
  }
  cout << res << endl;
  return 0;
}
