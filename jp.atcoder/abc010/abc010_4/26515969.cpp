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
#include <limits>


namespace graph_theory {
  namespace maximum_flow {
    template <typename T> struct FordFulkersonData { T capacity; };
    template <typename T> using FordFulkersonGraph = DenseDirectedGraph<void *, FordFulkersonData<T>>;

    template <typename T>
    T ford_fulkerson(FordFulkersonGraph<T> g, int src, int sink) {
      int n = g.nodes.size();
      T inf = std::numeric_limits<T>::max();
      std::vector<bool> visited(n);

      std::function<T(int, T)> augment_flow = [&](int u, T flow_in) -> T {
        visited[u] = true;
        if (u == sink) return flow_in;
        for (int v = 0; v < n; v++) {
          auto &data = g.edges[u][v];
          if (visited[v] || data.capacity == 0) continue;
          T flow = augment_flow(v, std::min(flow_in, data.capacity));
          if (flow == 0) continue;
          data.capacity -= flow;
          g.edges[v][u].capacity += flow;
          return flow;
        }
        return 0;
      };

      T flow = 0;
      while (1) {
        std::fill(visited.begin(), visited.end(), false);
        T f = augment_flow(src, inf);
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
  using G = graph_theory::maximum_flow::FordFulkersonGraph<int>;
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
  std::cout << graph_theory::maximum_flow::ford_fulkerson(g, 0, n) << '\n';
}
