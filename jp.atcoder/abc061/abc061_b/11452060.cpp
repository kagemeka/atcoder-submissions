#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<int> cnt(n);
  int a, b;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    cnt[a-1]++;
    cnt[b-1]++;
  }
  for (int i = 0; i < n; i++) {cout << cnt[i] << '\n';}
  return 0;

}
