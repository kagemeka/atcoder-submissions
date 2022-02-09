#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> x(n);
  vector<int> y(n);
  for (int i = 0; i < n; i++) cin >> x[i] >> y[i];
  double s = 0;
  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      s += sqrt(pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2));
    }
  }
  cout << setprecision(7) << s * 2 / n << '\n';
  return 0;
}
