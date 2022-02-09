#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  double p = 1;
  double s = 0;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    p *= a;
    s += a;
  }
  if (n == 1) {
    cout << s << '\n';
  } else {
    cout << setprecision(6) << p / (s * (n - 1)) << '\n';
  }
  return 0;
}
