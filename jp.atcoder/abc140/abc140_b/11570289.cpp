#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> a(n);
  vector<int> b(n);
  vector<int> c(n-1);
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n; i++) cin >> b[i];
  for (int i = 0; i < n - 1; i++) cin >> c[i];

  int tot = 0;
  for (int i = 0; i < n; i++) {
    tot += b[i];
    if (i < n - 1) {
      tot += (a[i+1] == a[i] + 1) * c[a[i]-1];
    }
  }
  cout << tot << '\n';
  return 0;
}
