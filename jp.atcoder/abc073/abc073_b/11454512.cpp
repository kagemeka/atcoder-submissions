#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int l, r;
  int tot = 0;
  for (int i = 0; i < n; i++) {
    cin >> l >> r;
    tot += r - l + 1;
  }
  cout << tot << '\n';
  return 0;
}
