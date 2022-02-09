#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> h(n);
  for (int i = 0; i < n; i++) cin >> h[i];
  int cnt = 0;
  int hmax = *max_element(h.begin(), h.end());
  for (int i = 0; i < hmax; i++) {
    bool flag = false;
    for (int j = 0; j < n; j++) {
      if (h[j] == 0) flag = false;
      else {
        if (!flag) {
          flag = true;
          cnt++;
        }
        h[j]--;
      }
    }
  }
  cout << cnt << '\n';
  return 0;
}
