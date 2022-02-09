#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> cnt(9);
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    cnt[min(a, 3200) / 400]++;
  }
  int mi = 0, ma = 0;
  for (int i = 0; i < 8; i++) {
    mi += !!cnt[i];
  }
  ma = mi + cnt[8];
  mi = max(1, mi);
  cout << mi << " " << ma << '\n';
  return 0;
}
