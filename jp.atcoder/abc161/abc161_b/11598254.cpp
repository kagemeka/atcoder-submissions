#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<int> a(n);
  int s = 0;
  for (int i = 0; i < n; i++) {
    int tmp;
    cin >> tmp;
    a[i] = tmp;
    s += tmp;
  }
  sort(a.begin(), a.end(), greater<int>());
  string ans = (a[m-1] * 4 * m >= s) ? "Yes" : "No";
  cout << ans << '\n';
  return 0;
}
