#include <bits/stdc++.h>
using namespace std;

int s(int n) {
  int tot = 0;
  while (n) {
    tot += n % 10;
    n /= 10;
  }
  return tot;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  string ans = (n % s(n)) ? "No" : "Yes";
  cout << ans << '\n';
  return 0;
}
