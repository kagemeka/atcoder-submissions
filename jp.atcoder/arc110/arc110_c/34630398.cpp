#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n);
  vector<int> idx(n);
  for(int i = 0; i < n; i++) {
    cin >> p[i];
    p[i]--;
    idx[p[i]] = i;
  }
  vector<bool> swapped(n);
  vector<int> res;
  for(int i = 0; i < n; i++) {
    int j = idx[i];
    while(i < j) {
      idx[p[j - 1]] = j;
      idx[i] = j - 1;
      swap(p[j - 1], p[j]);
      if(swapped[j - 1]) {
        cout << -1 << endl;
        return 0;
      }
      swapped[j - 1] = true;
      res.push_back(j);
      j--;
    }
  }
  if((int)res.size() != n - 1) {
    cout << -1 << endl;
    return 0;
  }
  for(auto& i: res) { cout << i << '\n'; }
}
