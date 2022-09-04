#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n);
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    x--;
    p[i] = x;
  }
  // simulation
  int t = 100000;
  vector<pair<char, int>> ops;
  vector<bool> is_odd(n);
  for(int i = 0; i < n; i++) { is_odd[p[i]] = (p[i] - i) & 1; }
  // for (int i = 0; i < n; i++) {
  // }
  for(int i = 0; i < n; i++) {
    int j = i;
    while(j < n) {
      if(p[j] == i) break;
      j++;
    }
    // bool is_odd = (j - i) & 1 == 1;
    while(i + 2 <= j) {
      if(is_odd[i] && is_odd[p[j - 1]]) {
        is_odd[i] = false;
        is_odd[p[j - 1]] = false;
        swap(p[j - 1], p[j]);
        ops.emplace_back('A', j - 1);
        j--;
        t--;
        continue;
      }
      ops.emplace_back('B', j - 2);
      swap(p[j - 2], p[j]);
      j -= 2;
      t -= 2;
    }
    if(j != i) {
      ops.emplace_back('A', i);
      is_odd[p[i]] = is_odd[p[i]] ^ true;
      swap(p[i], p[j]);
      j--;
      t--;
    }
    assert(i == j);
  }
  assert(t >= 0);
  for(int i = 0; i < n; i++) assert(p[i] == i);
  cout << ops.size() << endl;
  for(auto& [c, i]: ops) { cout << c << ' ' << i + 1 << '\n'; }
  // minimize A
}
