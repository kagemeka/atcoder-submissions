#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  int ans = k * pow(k-1, n-1);
  cout << ans << '\n';
  return 0;
}
