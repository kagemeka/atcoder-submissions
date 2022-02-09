#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<bitset<10>> info(n);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 10; j++) {
      int f; cin >> f;
      info[i][j] = f;
    }
  }
  vector<vector<int>> p(n, vector<int>(11));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < 11; j++) {
      cin >> p[i][j];
    }
  }
  int ans = -1001001001;
  for (int i = 1; i < (1 << 10); i++) {
    bitset<10> comb(i);
    int score = 0;
    for (int j = 0; j < n; j++) {
      score += p[j][(comb & info[j]).count()];
    }
    ans = max(ans, score);
  }
  cout << ans << '\n';
  return 0;

}
