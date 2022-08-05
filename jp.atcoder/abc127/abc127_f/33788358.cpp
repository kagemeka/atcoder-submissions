#include <bits/stdc++.h>
using namespace std;
template<typename T> class median_queue {
  using Self = median_queue;
  multiset<T> lo_set, hi_set;

public:
  median_queue() = default;
  [[nodiscard]] auto size() const -> int {
    return lo_set.size() + hi_set.size();
  }
  auto top() -> T { return *lo_set.rbegin(); }
  auto insert(T x) {
    if(size() & 1) {
      lo_set.insert(x);
      auto ptr = --lo_set.end();
      x = *ptr;
      lo_set.erase(ptr);
      hi_set.insert(x);
    } else {
      hi_set.insert(x);
      auto ptr = hi_set.begin();
      x = *ptr;
      hi_set.erase(ptr);
      lo_set.insert(x);
    }
  }
};
auto main() -> int {
  int q;
  cin >> q;
  long s = 0;
  median_queue<int> st;
  int const inf = 1 << 30;
  st.insert(-inf);
  st.insert(inf);
  int m = st.top();
  while(q--) {
    int t;
    cin >> t;
    if(t == 2) {
      cout << m << ' ' << s << endl;
    } else {
      int a, b;
      cin >> a >> b;
      s += b;
      if(st.size() & 1 || a < m) {
        s += abs(a - m);
        st.insert(a);
        m = st.top();
      } else {
        st.insert(a);
        m = st.top();
        s += max(0, a - m);
      }
    }
  }
}
