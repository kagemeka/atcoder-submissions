#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> h(n);
  for (int i = 0; i < n; i++) cin >> h[i];
  string ans = "Yes";

  for (int i = n - 1; i > 0; i--) {
    if (h[i-1] > h[i]) h[i-1]--;
    if (h[i-1] > h[i]) {
      ans = "No";
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
