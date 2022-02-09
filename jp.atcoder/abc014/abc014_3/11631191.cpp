#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int m = 1000001;
  vector<int> res(m + 1);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int l, r;
    cin >> l >> r;
    res[l]++;
    res[r+1]--;
  }
  for (int i = 0; i < m; i++) res[i+1] += res[i];
  cout << *max_element(res.begin(), res.end()) << '\n';
  return 0;
}
