#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k;
  cin >> n >> k;
  bitset<1001> res(0);
  for (int i = 0; i < k; i++) {
    int d; cin >> d;
    for (int j = 0; j < d; j++) {
      int a; cin >> a; a--;
      res.set(a);
    }
  }
  cout << n - res.count() << '\n';
  return 0;
}
