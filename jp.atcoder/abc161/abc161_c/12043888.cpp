#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long n, k; cin >> n >> k;
  n %= k;
  cout << min(n, k - n) << '\n';
  return 0;
}
