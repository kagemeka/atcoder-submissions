#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> in_deg(n);
  for(int i = 0; i < n - 1; i++) {
    int a;
    cin >> a;
    a--;
    in_deg[a]++;
  }
  for(int i = 0; i < n; i++) cout << in_deg[i] << endl;
}
