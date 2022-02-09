#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> d(n);
  for (int i = 0; i < n; i++) cin >> d[i];
  sort(d.begin(), d.end());
  int m = n / 2;
  int l = d[m-1], r = d[m];
  cout << r - l << '\n';
  return 0;
}
