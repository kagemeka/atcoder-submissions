#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, q;
  cin >> n >> q;
  vector<int> res(n + 1);
  for (int i = 0; i < q; i++) {
    int l, r;
    cin >> l >> r;
    l--; r--;
    res[l]++;
    res[r+1]--;
  }
  for (int i = 0; i < n; i++) {
    res[i+1] += res[i];
  }
  for (int i = 0; i < n; i++) {
    cout << (res[i] & 1);
  }
  cout << '\n';
  return 0;
}
