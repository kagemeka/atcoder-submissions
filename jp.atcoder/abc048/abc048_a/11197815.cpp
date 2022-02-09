#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<string> s(3);
  for (int i = 0; i < 3; i++) {
    cin >> s[i];
  }
  string res;
  for (int i = 0; i < 3; i++) {
    res += s[i][0];
  }
  cout << res << endl;
  return 0;
}
