#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  unordered_set<int> loop_start = {1, 2, 4};
  for (int i = 0; i < 1e6; i++) {
    if (loop_start.find(n) != loop_start.end()) {
      cout << i + 4 << '\n';
      return 0;
    }
    n = (n & 1) ? 3 * n + 1 : n / 2;
  }
  return 0;
}
