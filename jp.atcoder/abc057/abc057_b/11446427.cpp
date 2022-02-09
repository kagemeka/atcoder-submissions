#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  vector<tuple<int, int>> ab(n);
  vector<tuple<int, int>> cd(m);
  int x, y;
  for (int i = 0; i < n; i++) {
    cin >> x >> y;
    ab[i] = make_tuple(x, y);
  }
  for (int i = 0; i < m; i++) {
    cin >> x >> y;
    cd[i] = make_tuple(x, y);
  }

  for (tuple<int, int> &ab : ab) {
    int a, b;
    a = get<0>(ab);
    b = get<1>(ab);
    int dist = 1001001001;
    int p;
    for (int i = 0; i < m; i++) {
      int c, d;
      c = get<0>(cd[i]);
      d = get<1>(cd[i]);
      int tmp = abs(c - a) + abs(d - b);
      if (tmp < dist) {
        dist = tmp;
        p = i + 1;
      }
    }
    cout << p << '\n';
  }
  return 0;
}
