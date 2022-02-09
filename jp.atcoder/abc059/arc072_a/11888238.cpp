#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];

  long long c1 = 0, c2 = 0, s1 = 0, s2 = 0;
  for (int i = 0; i < n; i++) {
    s1 += a[i];
    s2 += a[i];
    if (i & 1) {
      if (s1 >= 0) {c1 += s1 + 1; s1 = -1;}
      if (s2 <= 0) {c2 += 1 - s2; s2 = 1;}
    } else {
      if (s1 <= 0) {c1 += 1 - s1; s1 = 1;}
      if (s2 >= 0) {c2 += s2 + 1; s2 = -1;}
    }
  }
  cout << min(c1, c2) << '\n';
  return 0;
}
