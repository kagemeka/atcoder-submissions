#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  string ans = "No";
  for (int i = 1; i < 10; i++) {
    if (n % i) continue;
    int j = n / i;
    if (j >= 1 && j <= 9) {
      ans = "Yes";
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
