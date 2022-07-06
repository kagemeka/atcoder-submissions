#include <bits/stdc++.h>
using namespace std;

template<typename T> class median_queue {
  using Self = median_queue;
  priority_queue<T> lo_que;
  priority_queue<T, vector<T>, greater<>> hi_que;

public:
  median_queue() = default;

  [[nodiscard]] auto size() const -> int {
    return lo_que.size() + hi_que.size();
  }

  auto top() -> T { return lo_que.top(); }

  auto insert(T x) {
    if(size() & 1) {
      lo_que.push(x);
      hi_que.push(lo_que.top());
      lo_que.pop();
    } else {
      hi_que.push(x);
      lo_que.push(hi_que.top());
      hi_que.pop();
    }
  }
};

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int q;
  cin >> q;

  median_queue<int> que;

  long s = 0;
  while(q--) {
    int t;
    cin >> t;
    if(t == 1) {
      int a, b;
      cin >> a >> b;
      s += b;
      int prev = que.size() ? que.top() : a;
      s += abs(a - prev);
      que.insert(a);
      if(que.size() & 1) s -= abs(prev - que.top());
    } else {
      cout << que.top() << ' ' << s << endl;
    }
  }
}