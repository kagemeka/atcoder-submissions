#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  int tot = 0;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    tot += min(x, k - x) * 2;
  }
  cout << tot << '\n';
  return 0;
}
