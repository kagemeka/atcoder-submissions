#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k; cin >> n >> k;
  cout << (n + k - 3) / (k - 1) << '\n';
  return 0;
}
