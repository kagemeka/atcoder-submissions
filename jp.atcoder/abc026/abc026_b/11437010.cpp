#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> r(n);
  for (int i = 0; i < n; i++) {
    cin >> r[i];
  }
  sort(r.begin(), r.end());
  vector<double> s(n+1);
  for (int i = 0; i < n; i++) {
    s[i+1] = acos(-1) * pow(r[i], 2);
  }

  double tot = 0;
  for (int i = n; i > 0; i -= 2) {
    tot += s[i] - s[i-1];
  }
  cout << setprecision(15) << tot << '\n';
  return 0;

}
