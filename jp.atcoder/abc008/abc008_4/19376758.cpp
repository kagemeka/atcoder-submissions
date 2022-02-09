#include <bits/stdc++.h>
using namespace std;


class Solver {

private:

int w, h;
int n;
vector<int> x;
vector<int> y;

void prepare() {
  cin >> w >> h >> n;
  x = y = vector<int>(n);
  for (int i = 0; i < n; i++)
  {
    cin >> x[i] >> y[i];
    x[i]--; y[i]--;
  }
}

using Tup =
  tuple<int, int, int, int>;

map<Tup, long long> cache;

long long count(
  int x0, int y0,
  int x1, int y1
) {
  Tup t = Tup(x0, y0, x1, y1);
  if (cache.count(t))
  {
    return cache[t];
  }
  long long cnt = 0;
  for (int i = 0; i < n; i++)
  {
    if (x[i] < x0) continue;
    if (y[i] < y0) continue;
    if (x[i] >= x1) continue;
    if (y[i] >= y1) continue;

    long long tot =
      x1 - x0 + y1 - y0 - 1;
    tot += count(
      x0, y0, x[i], y[i]);
    tot += count(
      x0, y[i]+1, x[i], y1);
    tot += count(
      x[i]+1, y0, x1, y[i]);
    tot += count(
      x[i]+1, y[i]+1, x1, y1);

    cnt = max(cnt, tot);
  }
  return cache[t] = cnt;
}


void solve() {
  long long res;
  res = count(0, 0, w, h);
  cout << res << '\n';
}

public:

void run() {
  prepare();
  solve();
}

};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    Solver solver;
    solver.run();
  }

  return 0;
}
