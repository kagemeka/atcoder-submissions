#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> r(n);
  for (int i = 0; i < n; i++) {
    cin >> r[i];
  }

  sort(r.begin(), r.end(), greater<int>());

  double rate = 0;
  for (int i = k - 1; i > -1; i--) {
    rate = (rate + r[i]) / 2.0;
  }
  cout << setprecision(10) << rate << endl;
  return 0;

}
