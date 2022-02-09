#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> p(n);
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    int p;
    cin >> p;
    cnt += p != i + 1;
  }
  string ans = (cnt <= 2) ? "YES" : "NO";
  cout << ans << '\n';
  return 0;
}
