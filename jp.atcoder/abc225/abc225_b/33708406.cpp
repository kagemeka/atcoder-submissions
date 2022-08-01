#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> deg(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    deg[--u]++;
    deg[--v]++;
  }
  cout << (*max_element(deg.begin(), deg.end()) == n - 1 ? "Yes" : "No")
       << endl;
}
