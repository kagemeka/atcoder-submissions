#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<int> p(n);
  for(int i = 0; i < n; i++) cin >> p[i];

  vector<int> index(n);
  for(int i = 0; i < n; i++) index[p[i] - 1] = i;

  multiset<int> s;
  s.insert(-1);
  s.insert(-1);
  s.insert(n);
  s.insert(n);

  long tot = 0;

  for(int x = n; x > 0; x--) {
    int i = index[x - 1];
    s.insert(i);
    auto ptr = s.lower_bound(i);
    assert(*ptr == i);
    int j0 = *prev(prev(ptr));
    int j1 = *prev(ptr);
    int j2 = *next(ptr);
    int j3 = *next(next(ptr));
    tot += (long)x * (j1 - j0) * (j2 - i);
    tot += (long)x * (i - j1) * (j3 - j2);
  }
  cout << tot << endl;
}