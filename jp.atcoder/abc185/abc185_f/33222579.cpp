#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size(); }
  auto operate(int i, int x) {
    for(i++; i <= size(); i += i & -i) data[i] ^= x;
  }
  auto get(int i) -> int {
    int v = 0;
    for(; i > 0; i -= i & -i) v ^= data[i];
    return v;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  cin >> n >> q;
  fenwick fw(n);
  for(int i = 0; i < n; i++) {
    int a;
    cin >> a;
    fw.operate(i, a);
  }
  while(q--) {
    int t, x, y;
    cin >> t >> x >> y;
    --x;
    if(t == 1) {
      fw.operate(x, y);
    } else {
      cout << (fw.get(y) ^ fw.get(x)) << endl;
    }
  }
}
