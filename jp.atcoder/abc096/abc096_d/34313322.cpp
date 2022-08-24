#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int const k = 1 << 16;
  vector<bool> is_p(k, true);
  for(int i = 2; i * i < k; i++) {
    if(!is_p[i]) continue;
    for(int j = i * i; j < k; j += i) is_p[j] = false;
  }
  vector<int> a;
  for(int i = 2; i < k; i += 5) {
    if(is_p[i]) a.push_back(i);
    if((int)a.size() == n) break;
  }
  assert((int)a.size() == n);
  for(int i = 0; i < n; i++) cout << a[i] << " \n"[i == n - 1];
}
