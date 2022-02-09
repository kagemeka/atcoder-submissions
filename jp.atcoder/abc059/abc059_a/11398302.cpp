#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<string> ss(3);
  for (int i = 0; i < 3; i++) {
    cin >> ss[i];
  }
  string t = "";
  for (string s : ss) {
    t += toupper(s[0]);
  }
  cout << t << endl;
  return 0;
}
