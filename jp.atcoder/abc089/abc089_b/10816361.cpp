#include <bits/stdc++.h>
using namespace std;


int main() {
  int n;
  cin >> n;
  bool p, w, g, y;
  int cnt = 0;

  for (int i = 0; i < n; i++) {
    string c;
    cin >> c;
    if (c == "P") {
      if (!p) {
        cnt++;
        p = true;
      }
    } else if (c == "W") {
      if (!w) {
        cnt++;
        w = true;
      }
    } else if (c == "G") {
      if (!g) {
        cnt++;
        g = true;
      }
    } else if (c == "Y") {
      if (!y) {
        cnt++;
        y = true;
      }
    }
  }
  string ans;
  if (cnt == 3) {
    ans = "Three";
  } else {
    ans = "Four";
  }
  cout << ans << endl;
}
