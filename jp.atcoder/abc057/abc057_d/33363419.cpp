#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, a, b;
  cin >> n >> a >> b;
  vector<long> v(n);
  for(int i = 0; i < n; i++) cin >> v[i];
  sort(v.begin(), v.end());
  vector<vector<long>> p(n + 1, vector<long>(n + 1));
  for(int i = 0; i < n + 1; i++) p[i][0] = 1;
  for(int i = 1; i < n + 1; i++)
    for(int j = 1; j <= i; j++) { p[i][j] = p[i - 1][j - 1] + p[i - 1][j]; }
  long x = v[n - a];
  int c = a - (v.end() - upper_bound(v.begin(), v.end(), x));
  int d =
    upper_bound(v.begin(), v.end(), x) - lower_bound(v.begin(), v.end(), x);
  long tot = 0;
  if(c != a) {
    tot = p[d][c];
  } else {
    for(int i = c; i <= min(d, b - a + c); i++) { tot += p[d][i]; }
  }
  double avg = 0;
  for(int i = 0; i < a; i++) { avg += v[n - 1 - i]; }
  avg /= a;
  cout << setprecision(16) << avg << endl;
  cout << tot << endl;
}