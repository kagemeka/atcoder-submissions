#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, x;
  cin >> n >> x;
  x--;
  int m = 2 * n - 1;
  if(x == 0 || x == m - 1) {
    cout << "No" << endl;
    return 0;
  }
  cout << "Yes" << endl;
  vector<int> p(m, -1);
  set<int> st;
  for(int i = 0; i < m; i++) st.insert(i);
  if(n > 2) {
    vector<int> v;
    if(x == 1) v = {x + 1, x, x - 1, x + 2};
    else v = {x - 1, x, x + 1, x - 2};
    for(int i = 0; i < 4; i++) {
      p[n - 2 + i] = v[i];
      st.erase(v[i]);
    }
  }
  int i = -1;
  while(i < m - 1) {
    i++;
    if(p[i] != -1) { continue; }
    p[i] = *st.begin();
    st.erase(st.begin());
  }
  for(int i = 0; i < m; i++) { cout << p[i] + 1 << endl; }
}
