#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  unordered_set<int> ng;
  for (int i = 0; i < 3; i++) {
    int m;
    cin >> m;
    ng.insert(m);
  }
  string ans = "YES";
  if (ng.find(n) != ng.end()) {
    ans = "NO";
  } else {
    int cnt = 100;
    while (n) {
      if (cnt == 0) {
        ans = "NO";
        break;
      }
      bool flag = false;
      for (int i = 3; i > 0; i--) {
        if (ng.find(n - i) == ng.end()) {
          flag = true;
          n -= i;
          cnt--;
          break;
        }
      }
      if (!flag) {
        ans = "NO";
        break;
      }
      if (n <= 0) break;
    }
  }
  cout << ans << '\n';
  return 0;
}
