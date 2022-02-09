#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  vector<int> l(n);
  for (int i = 0; i < n; i++) {
    cin >> l[i];
  }
  sort(l.begin(), l.end(), greater<int>());
  cout << accumulate(l.begin(), l.begin() + k, 0) << '\n';
  return 0;
}
