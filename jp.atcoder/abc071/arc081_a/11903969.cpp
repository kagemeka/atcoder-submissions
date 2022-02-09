#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end(), greater<int>());
  long long y = 0, x = 0;
  for (int i = 0; i < n - 1; i++) {
    if (!y) {
      if (a[i] == a[i+1]) {
        y = a[i];
        i++;
      }
    } else {
      if (a[i] == a[i+1]) {
        x = a[i];
        break;
      }
    }
  }
  cout << y * x << '\n';
  return 0;
}
