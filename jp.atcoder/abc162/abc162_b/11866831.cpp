#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  long long res = 0;
  for (int i = 1; i < n + 1; i++) {
    res += (i % 3 && i % 5) ? i : 0;
  }
  cout << res << '\n';
  return 0;
}
