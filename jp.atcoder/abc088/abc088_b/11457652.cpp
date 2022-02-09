#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int a = 0, b = 0;
  vector<int> v(n);
  for (int i = 0; i < n; i++) {
    cin >> v[i];
  }
  sort(v.begin(), v.end(), greater<int>());
  for (int i = 0; i < n; i++) {
    (i & 1) ? b += v[i] : a += v[i];
  }
  cout << a - b << '\n';
  return 0;

}
