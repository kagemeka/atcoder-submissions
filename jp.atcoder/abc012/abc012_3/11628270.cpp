#include <bits/stdc++.h>
using namespace std;

set<int> divisors(int n) {
  set<int> res;
  for (int i = 1; i < floor(sqrt(n)) + 1; i++) {
    if (n % i == 0) {
      res.insert(i);
      res.insert(n / i);
    }
  }
  return res;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  n = 2025 - n;
  for (int const &i : divisors(n)) {
    if (i < 1 || i > 9) continue;
    int j = n / i;
    if (j < 1 || j > 9) continue;
    printf("%d x %d\n", i, j);
  }
  return 0;
}
