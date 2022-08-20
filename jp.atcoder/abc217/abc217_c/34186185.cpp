#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    x--;
    a[x] = i + 1;
  }
  for(int i = 0; i < n; i++) cout << a[i] << " \n"[i == n - 1];
}
