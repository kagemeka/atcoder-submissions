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
  for(int i = 0; i < n; i++) {
    int j = i;
    while(j < n) {
      if(p[j] == i) break;
      j++;
    }
    while(i + 2 <= j) {
      ops.emplace_back('B', j - 2);
      swap(p[j - 2], p[j]);
      j -= 2;
      t--;
    }
    if(j != i) {
      ops.emplace_back('A', i);
      swap(p[i], p[j]);
      j--;
      t--;
    }
    assert(i == j);
  }
  for(int i = 0; i < n; i++) assert(p[i] == i);
  cout << ops.size() << endl;
  for(auto& [c, i]: ops) { cout << c << ' ' << i + 1 << '\n'; }
}
