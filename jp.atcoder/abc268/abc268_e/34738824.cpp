#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // for each person, how many times he want to rotate ?
  // median
  int n;
  cin >> n;
  vector<int> p(n);
  for(int i = 0; i < n; i++) { cin >> p[i]; }
  vector<int> idx(n);
  for(int i = 0; i < n; i++) { idx[p[i]] = i; }
  vector<int> d(n);
  for(int i = 0; i < n; i++) d[i] = (i - idx[i] + n) % n;
  sort(d.begin(), d.end());
  int m = n / 2;
  int x = d[m];
  long s = 0;
  for(int i = 0; i < n; i++) {
    d[i] -= x;
    s += abs(d[i]);
  }
  cout << s << endl;
}
