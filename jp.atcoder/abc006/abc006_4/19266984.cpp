#include <bits/stdc++.h>
using namespace std;


template<typename T>
vector<T>
longest_increasing_seq(
  const vector<T>& a
) {
  vector<T> lis(
    a.size(),
    numeric_limits<T>::max()
  );
  for (const T& x: a) {
    *lower_bound(
      lis.begin(),
      lis.end(),
      x
    ) = x;
  }
  return lis;
}


class Solver {

int n;
vector<int> c;

void prepare() {
  cin >> n;
  c = vector<int>(n);
  for (int i = 0; i < n; i++) {
    cin >> c[i];
  }
}


void solve() {
  auto lis =
    longest_increasing_seq(c);
  int inf =
    numeric_limits<int>::max();
  int i = lower_bound(
    lis.begin(),
    lis.end(),
    inf
  ) - lis.begin();
  cout << n - i << '\n';
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
