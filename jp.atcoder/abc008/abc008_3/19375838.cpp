#include <bits/stdc++.h>
using namespace std;


class Solver {

int n;
vector<long long> c;

void prepare() {
  cin >> n;
  c = vector<long long>(n);
  for (int i = 0; i < n; i++)
  {
    cin >> c[i];
  }
}


void solve() {
  map<long long, int> cnt;
  for (const long long& i: c)
  {
    for (const long long& j: c)
    {
      if (j % i != 0) continue;
      cnt[i]++;
    }
    cnt[i]--;
  }
  double ev = 0;
  for (const auto& p: cnt)
  {
    int i = p.second;
    ev += (double)(i/2 + 1)
      / (i+1);
  }
  printf("%.10f\n", ev);

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
