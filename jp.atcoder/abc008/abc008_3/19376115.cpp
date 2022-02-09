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
  vector<int> cnt(n);
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      cnt[i] += c[i]%c[j] == 0;
    }
    cnt[i]--;
  }

  double ev = .0;
  for (const int& i: cnt)
  {
    ev += (i / 2 + 1)
      / (double)(i + 1);
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
