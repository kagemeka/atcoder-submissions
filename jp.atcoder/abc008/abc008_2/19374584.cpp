#include <bits/stdc++.h>
using namespace std;


class Solver {

private:

int n;
vector<string> s;

void prepare() {
  cin >> n;
  s = vector<string>(n);
  for (int i = 0; i < n; i++)
  {
    cin >> s[i];
  }
}


void solve() {
  map<string, int> votes;
  for (const string& i: s)
  {
    votes[i]++;
  }
  using P = pair<string, int>;
  auto res = vector<P>(
    votes.begin(),
    votes.end()
  );
  sort(
    res.begin(),
    res.end(),
    [](
      const P& a,
      const P& b
    ) {
      return
        a.second > b.second;
    }
  );
  cout << res[0].first << '\n';

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
