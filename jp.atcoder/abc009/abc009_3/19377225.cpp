#include <bits/stdc++.h>
using namespace std;


class Solver {

private:

int n, k;
string s;

void prepare() {
  cin >> n >> k >> s;
}


void solve() {
  using Tup =
    tuple<int, int, int>;

  vector<int> cost(n, 1);
  for (int i = 0; i < n; i++)
  {
    priority_queue<
      Tup,
      vector<Tup>,
      greater<Tup>
    > que;

    for (
      int j = i+1; j < n; j++
    ) {
      if (s[j] >= s[i])
      {
        continue;
      }

      que.push(
        Tup(
          s[j],
          cost[i] + cost[j],
          -j
        )
      );
    }

    while (!que.empty())
    {
      Tup t = que.top();
      que.pop();
      char ch;
      int co, j;
      tie(ch, co, j) = t;
      j *= -1;
      if (co > k) continue;
      k -= co;
      swap(s[i], s[j]);
      cost[i] = cost[j] = 0;
      break;
    }
  }
  cout << s << '\n';
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
