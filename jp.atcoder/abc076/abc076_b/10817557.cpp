#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  int res = 1;
  for (int i = 0; i < n; i++) {
    if (res <= k) {
      res *= 2;
    } else {
      res += k;
    }
  }
  cout << res << endl;
}
