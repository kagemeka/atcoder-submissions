#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<bitset<10>> friends(n);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    friends[a].set(b);
    friends[b].set(a);
  }
  for (int i = 0; i < n; i++) {
    bitset<10> res(0);
    for (int j = 0; j < n; j++) {
      if (friends[i][j]) {
        for (int k = 0; k < n; k++) {
          if (friends[j][k]) res.set(k);
        }
      }
    }
    res.reset(i);
    for (int j = 0; j < n; j++) {
      if (friends[i][j]) res.reset(j);
    }
    cout << res.count() << '\n';
  }
  return 0;
}
