#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  int f = -n;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    f += a;
  }
  cout << f << '\n';
  return 0;
}
