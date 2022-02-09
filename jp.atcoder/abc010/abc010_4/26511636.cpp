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
    template <typename T> struct DinicData { T capacity; };
    template <typename T> using DinicGraph = SparseDirectedGraph<void *, DinicData<T>>;

    template <typename T>
    T dinic(DinicGraph<T> g, int src, int sink) {
      int n = g.nodes.size();
      std::vector<int> level(n, -1);
      std::function<void()> update_level = [&]() -> void {
        for (int i = 0; i < n; i++) level[i] = -1;
        level[src] = 0;
        std::queue<int> fifo_que;
        fifo_que.push(src);
        while (!fifo_que.empty()) {
          int u = fifo_que.front(); fifo_que.pop();
          for (const auto &e : g.edges[u]) {
            if (level[e.v] != -1 || e.data.capacity <= 0) continue;
            level[e.v] = level[u] + 1;
            fifo_que.push(e.v);
          }
        }
      };

      std::function<T(int, T)> flow_to_sink = [&](int u, T flow_in) -> T {
        if (u == sink) return flow_in;
        if (flow_in == 0) return 0;
        T flow_out = 0;
        auto edges = g.edges[u];
        g.edges[u].clear();
        for (auto &e : edges) {
          if (e.data.capacity == 0) continue;
          if (level[e.v] <= level[u]) {g.add_edge(e); continue;}
          T flow = flow_to_sink(e.v, std::min(flow_in, e.data.capacity));
          if ((e.data.capacity -= flow) > 0) g.add_edge(e);
          if (flow > 0) g.edges[e.v].push_back({e.v, u, {flow}});
          flow_in -= flow;
          flow_out += flow;
        }
        return flow_out;
      };


      T inf = std::numeric_limits<T>::max();
      T flow = 0;
      while (1) {
        update_level();
        if (level[sink] == -1) return flow;
        flow += flow_to_sink(src, inf);
      }
    };
  };

  // e.g. using G = graph_theory::maximum_flow::DinicGraph<long long>;
};




int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int n, k, m;
  std::cin >> n >> k >> m;
  using G = graph_theory::maximum_flow::DinicGraph<int>;
  G g(n + 1);
  while (k--) {
    int p; std::cin >> p;
    g.add_edge({p, n, {1}});
  }
  while (m--) {
    int a, b; std::cin >> a >> b;
    g.add_edge({a, b, {1}});
    g.add_edge({b, a, {1}});
  }
  std::cout << graph_theory::maximum_flow::dinic(g, 0, n) << '\n';
}
