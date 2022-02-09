#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    a[i] -= i + 1;
  }
  sort(a.begin(), a.end());
  int b = a[n/2];
  long long s = 0;
  for (int &x : a) {
    s += abs(x - b);
  }
  cout << s << '\n';
  return 0;
}
