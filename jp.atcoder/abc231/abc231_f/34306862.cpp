#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1){};
  auto size() -> int { return data.size() - 1; }
  auto add(int i, int x) {
    for(i++; i <= size(); i += i & -i) data[i] += x;
  }
  auto get(int i) -> int {
    int v = 0;
    for(; i > 0; i -= i & -i) v += data[i];
    return v;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<pair<int, int>> ab(n);
  for(int i = 0; i < n; i++) cin >> ab[i].first;
  for(int i = 0; i < n; i++) cin >> ab[i].second;
  sort(ab.begin(), ab.end(), [&](auto x, auto y) {
    if(x.first != y.first) {
      return x.first < y.first;
    } else {
      return x.second > y.second;
    }
  });
  vector<int> b(n);
  int c = 0;
  long s = 0;
  for(int i = 0; i < n; i++) {
    b[i] = ab[i].second;
    if(i < n && ab[i] == ab[i + 1]) {
      c++;
    } else {
      s += (long)c * (c - 1) >> 1;
      c = 1;
    }
  }
  auto v = b;
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()), v.end());
  auto get = [&](int x) -> int {
    return lower_bound(v.begin(), v.end(), x) - v.begin();
  };
  fenwick fw(n);
  for(int i = 0; i < n; i++) {
    auto& x = b[i];
    x = get(x);
    s += i + 1 - fw.get(x);
    fw.add(x, 1);
  }
  // for(int i = 0; i < n; i++) cout << b[i] << '\n';
  cout << s << endl;
}
