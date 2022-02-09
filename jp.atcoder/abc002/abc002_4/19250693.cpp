#include <bits/stdc++.h>
using namespace std;


namespace Algebra {

template<typename T> int bit_length(T n) {
  int length = 0;
  while (n) {
    n >>= 1;
    length++;
  };
  return length;
}

template<typename T>
int bit_count(T n) {
  int cnt = 0;
  int l = bit_length(n);
  while (l--) {
    cnt += n & 1;
    n >>= 1;
  };
  return cnt;
}

}
using namespace Algebra;


void solve(
  int n,
  int m,
  vector<int> x,
  vector<int> y
) {
  vector<int> relations(n, 0);
  for (int i = 0; i < m; i++) {
    relations[x[i]] |= 1<<y[i];
    relations[y[i]] |= 1<<x[i];
  }
  int cnt = 0;
  for (int s = 0; s < 1<<n; s++)
  {
    int t = (1 << n) - 1;
    for (int i = 0; i < n; i++)
    {
      if (~s>>i&1) continue;
      t &= relations[i] | 1<<i;
    }
    if ((s&t) != s) continue;
    cnt = max(
      cnt,
      bit_count(s)
    );
  }
  cout << cnt << '\n';
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<int> x(m), y(m);
  for (int i = 0; i < m; i++) {
    cin >> x[i] >> y[i];
    x[i]--; y[i]--;
  }
  solve(n, m, x, y);

  return 0;
}
