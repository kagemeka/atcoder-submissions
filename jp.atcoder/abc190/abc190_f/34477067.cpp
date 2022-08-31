#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size() - 1; }
  auto add(int i, int x) {
    for(i++; i <= size(); i += i & -i) data[i] += x;
  }
  auto sum(int i) -> int {
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
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  fenwick fw(n);
  long cnt = 0;
  for(int i = 0; i < n; i++) {
    int& x = a[i];
    cnt += i - fw.sum(x);
    fw.add(x, 1);
  }
  cout << cnt << '\n';
  for(int i = 0; i < n - 1; i++) {
    int x = a[i];
    cnt += n - 1 - 2 * x;
    cout << cnt << '\n';
  }
}
