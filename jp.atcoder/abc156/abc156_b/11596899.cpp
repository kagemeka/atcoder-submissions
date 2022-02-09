#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k;
  cin >> n >> k;
  int cnt = 0;
  while (n) {
    n /= k;
    cnt++;
  }
  cout << cnt << '\n';
  return 0;
}
