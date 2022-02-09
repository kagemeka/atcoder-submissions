#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c, k, s, t;
  cin >> a >> b >> c >> k >> s >> t;
  int tot = a*s + b*t;
  if (s + t >= k) tot -= c * (s + t);
  cout << tot << endl;
  return 0;
}
