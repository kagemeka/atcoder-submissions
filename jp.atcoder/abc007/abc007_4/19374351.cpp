#include <bits/stdc++.h>
using namespace std;


class Solver {

long long a, b;
set<int> ng = {4, 9};


void prepare() {
  cin >> a >> b;
}

template<typename T>
T count(T n)
{
  string x = to_string(n);
  bool flg = true;
  T cnt = 0;
  for (const char& i: x)
  {
    int d = i - '0';
    cnt *= 8;
    if (!flg) continue;
    cnt += d - (d > 4);
    if (ng.count(d))
    {
      flg = false;
    }
  }
  cnt += flg;
  return n - cnt;
}


void solve() {
  long long res;
  res = count(b) - count(a-1);
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
