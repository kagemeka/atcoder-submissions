#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;

  long long cap = 1001001001001001;
  for (int i = 0; i < 5; i++) {
    long long c; cin >> c;
    cap = min(cap, c);
  }
  cout << (n + cap - 1) / cap + 4 << '\n';
  return 0;
}
