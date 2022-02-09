#include <bits/stdc++.h>
using namespace std;


template<typename T>
struct Edge {

public:

T weight, capacity;

Edge(
  T weight=1, T capacity=1
)
: weight(weight),
  capacity(capacity)
{}
};


template<typename T>
struct Node {};


template<typename T>
struct Graph {

public:

Graph(int n=0)
: edges(n), nodes(n)
{}

void add_edge(
  int u, int v,
  T weight=1, T capacity=1
) {
  edges[u].emplace(
    v,
    Edge<T>(weight, capacity)
  );
}

vector<map<int, Edge<T>>>
  edges;

vector<Node<T>> nodes;


vector<int> level;


void bfs(int source=0)
{
  int n = (int)nodes.size();
  level = vector<int>(n, -1);
  level[source] = 0;
  queue<int> que;
  que.push(source);
  while (!que.empty())
  {
    int u = que.front();
    que.pop();
    for (
      const auto& p: edges[u])
    {
      int v = p.first;
      Edge<T> e = p.second;
      if (level[v] != -1)
      {
        continue;
      }
      level[v] = level[u] + 1;
      que.push(v);
    }
  }
}

};


class Solver {

int r, c, sy, sx, gy, gx, n;
vector<char> maze;


void prepare() {
  cin >> r >> c >> sy >> sx
    >> gy >> gx;
  sy--; sx--; gy--; gx--;
  n = r * c;
  maze = vector<char>(n);
  for (int i = 0; i < n; i++) {
    cin >> maze[i];
  }
}


void solve() {
  int src = sy * c + sx;
  int dst = gy * c + gx;

  Graph<int> g(n);

  vector<int> delta = {
    -c, -1, 1, c
  };

  for (int i = 0; i < n; i++)
  {
    if (maze[i] == '#')
    {
      continue;
    }
    vector<int> nx;
    if (i >= c) {
      nx.push_back(i - c);
    }
    if (i <= n-c) {
      nx.push_back(i + c);
    }
    if (i%c != 0) {
      nx.push_back(i - 1);
    }
    if (i%c != c-1) {
      nx.push_back(i + 1);
    }
    for (const int& j: nx)
    {
      if (maze[j] == '#')
      {
        continue;
      }
      g.add_edge(i, j);
    }
  }
  g.bfs(src);
  cout << g.level[dst] << '\n';


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
