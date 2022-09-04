#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n);
  vector<bool> is_odd(n);
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    x--;
    p[i] = x;
    is_odd[i] = (x - i) & 1;
  }
  vector<pair<char, int>> ops;
  for(int i = 0; i < n; i++) {
    if(!is_odd[i]) continue;
    int j = i;
    while(j >= 2 && !is_odd[j - 2]) {
      swap(p[j - 2], p[j]);
      ops.emplace_back('B', j - 2);
      is_odd[j - 2] = true;
      is_odd[j] = false;
      j -= 2;
    }
  }
  for(int i = 0; i < n; i += 2) {
    if(!is_odd[i]) break;
    assert(is_odd[i + 1]);
    swap(p[i], p[i + 1]);
    ops.emplace_back('A', i);
    is_odd[i] = false;
    is_odd[i + 1] = false;
  }
  for(int i = 0; i < n; i++) {
    int j = i;
    while(j < n) {
      if(p[j] == i) break;
      j++;
    }
    assert(((j - i) & 1) == 0);
    while(j > i) {
      ops.emplace_back('B', j - 2);
      swap(p[j - 2], p[j]);
      j -= 2;
    }
  }
  cout << ops.size() << '\n';
  for(auto& [c, i]: ops) { cout << c << ' ' << i + 1 << '\n'; }
}
