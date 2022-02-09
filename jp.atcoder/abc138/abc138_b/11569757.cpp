#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> a(n);
  int p = 1;
  int s = 0;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    s += a[i];
    p *= a[i];
  }
  int denom = 0;
  for (int i = 0; i < n; i++) denom += p / a[i];
  cout << setprecision(7) << (double)p / (double)denom << '\n';
  return 0;
}
