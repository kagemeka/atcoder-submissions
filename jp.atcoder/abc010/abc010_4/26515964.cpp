#include <iostream>
#include <vector>


namespace graph_theory {
  template<typename T> struct Edge { const int u, v; T data; };


  template<typename T, typename U>
  struct SparseDirectedGraph {
    using E = Edge<U>;  // G::E edge{u, v, data};
    std::vector<T> nodes;
    std::vector<std::vector<E>> edges;
    SparseDirectedGraph(int n) : nodes(n), edges(n) {}
    void add_edge(const E &e) { edges[e.u].push_back(e); }
  };


  template <typename T, typename U>
  struct DenseDirectedGraph {
    std::vector<T> nodes;
    std::vector<std::vector<U>> edges;
    DenseDirectedGraph(int n) : nodes(n), edges(n, std::vector<U>(n)) {}
    std::vector<U>& operator[](int i) { return edges[i]; }
  };


  template <typename T, typename U>
  struct UndirectedGraph {
    using E = Edge<U>;
    std::vector<T> nodes;
    std::vector<E> edges;
    UndirectedGraph(int n) : nodes(n) {}
    SparseDirectedGraph<T, U> to_directed() const {
      SparseDirectedGraph<T, U> g(nodes.size());
      g.nodes = nodes;
      for (const E &e : edges) {
        g.add_edge(e);
        g.add_edge(E{e.v, e.u, e.data});
      };
      return g;
    }
  };
};


#include <vector>
#include <functional>
#include <queue>
#include <limits>


namespace graph_theory {
  namespace maximum_flow {
    template <typename T> struct EdmondsKarpData { T capacity; };
    template <typename T> using EdmondsKarpGraph = DenseDirectedGraph<void *, EdmondsKarpData<T>>;


    template <typename T>
    T edmonds_karp(EdmondsKarpGraph<T> g, int src, int sink) {
      int n = g.nodes.size();
      T inf = std::numeric_limits<T>::max();
      std::vector<int> prev(n, -1);
      std::vector<bool> visited(n);
      std::queue<int> fifo_que;

      std::function<void()> find_path = [&]() -> void {
        std::fill(prev.begin(), prev.end(), -1);
        std::fill(visited.begin(), visited.end(), false);
        visited[src] = true;
        fifo_que.push(src);
        while (!fifo_que.empty()) {
          int u = fifo_que.front(); fifo_que.pop();
          for (int v = 0; v < n; v++) {
            if (visited[v] || g.edges[u][v].capacity == 0) continue;
            visited[v] = true;
            prev[v] = u;
            fifo_que.push(v);
          }
        }
      };

      std::function<T()> augment_flow = [&]() -> T {
        int u, v = sink;
        T flow = inf;
        while (prev[v] != -1) {
          u = prev[v];
          flow = std::min(flow, g.edges[u][v].capacity);
          v = u;
        }
        if (flow == inf) return 0;
        v = sink;
        while (prev[v] != -1) {
          u = prev[v];
          g.edges[u][v].capacity -= flow;
          g.edges[v][u].capacity += flow;
          v = u;
        }
        return flow;
      };

      T flow = 0;
      while (1) {
        find_path();
        T f = augment_flow();
        if (f == 0) return flow;
        flow += f;
      }
    }
  };
};



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int n, k, m;
  std::cin >> n >> k >> m;
  using G = graph_theory::maximum_flow::EdmondsKarpGraph<int>;
  G g(n + 1);
  while (k--) {
    int p; std::cin >> p;
    g.edges[p][n] = {1};
  }
  while (m--) {
    int a, b; std::cin >> a >> b;
    g.edges[a][b] = {1};
    g.edges[b][a] = {1};
  }
  std::cout << graph_theory::maximum_flow::edmonds_karp(g, 0, n) << '\n';
}
