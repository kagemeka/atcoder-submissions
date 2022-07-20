#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1) {}
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
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int cnt = 0;
  fenwick fw(n);
  for(int i = n - 1; i >= 0; i--) {
    cnt += fw.get(a[i]);
    fw.add(a[i], 1);
  }
  for(int i = 0; i < n; i++) {
    cout << cnt << endl;
    cnt -= a[i];
    cnt += n - 1 - a[i];
  }
}
