#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  int sa = 0;
  int sb = 0;
  sort(a.begin(), a.end(), greater<int>());
  for (int i = 0; i < n; i++) {
    (i & 1) ? sb += a[i] : sa += a[i];
  }

  cout << sa - sb << endl;
  return 0;
}
