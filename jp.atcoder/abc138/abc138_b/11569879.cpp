#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  double denom;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    denom += 1.0 / a;
  }
  cout << setprecision(6) << 1 / denom << '\n';
  return 0;
}
