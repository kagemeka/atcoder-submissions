#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<int> a(3);
  for (int i = 0; i < 3; i++) cin >> a[i];
  sort(a.begin(), a.end());
  int d = a[2] * 2 - a[1] - a[0];
  if (d & 1) d += 3;
  cout << d / 2 << '\n';
  return 0;
}
