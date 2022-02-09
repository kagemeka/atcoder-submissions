#include <bits/stdc++.h>
using namespace std;

int main() {
  string n;
  cin >> n;
  int cnt = 1;

  string ans;
  bool flag = false;

  for (int i = 0; i < int(n.size()) - 1; i ++) {
    if (n[i+1] == n[i]) {
      cnt++;
      if (cnt == 3) {
        ans = "Yes";
        flag = true;
      }
    } else {
      cnt = 1;
    }
  }
  if (!flag) {
    ans = "No";
  }
  cout << ans << endl;
}
