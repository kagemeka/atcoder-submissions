#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  int const inf = 1 << 30;
  set<int> st;
  multiset<int> ds;
  for(int i = 0; i < w; i++) {
    st.insert(i);
    ds.insert(0);
  }
  st.insert(w);
  ds.insert(inf);
  vector<int> d(w + 1, 0);
  d[w] = inf;
  for(int i = 0; i < h; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    if(st.count(b)) {
      st.erase(b);
      ds.erase(ds.lower_bound(d[b]));
    }
    auto it = st.lower_bound(a);
    while(it != st.lower_bound(b)) {
      auto x = *it;
      it++;
      st.erase(x);
      ds.erase(ds.lower_bound(d[x]));
      if(b < w) { d[b] = min(d[b], d[x] + b - x); }
      d[x] = inf;
    }
    st.insert(b);
    ds.insert(d[b]);
    int res = *ds.begin();
    cout << (res == inf ? -1 : res + i + 1) << endl;
  }
}
