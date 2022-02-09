#include <bits/stdc++.h>
using namespace std;

int main() {
  string n;
  cin >> n;
  string ans = "No";
  for (char c : n) {
    if (c == '9') {
      ans = "Yes";
      break;
    }
  }
  cout << ans << endl;
  return 0;
}
