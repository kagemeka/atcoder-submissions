#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  int n2 = n * 2;
  vector<string> a(n2);
  for(int i = 0; i < n2; i++) cin >> a[i];
  vector<int> wins(n2);
  vector<int> arg(n2);
  iota(arg.begin(), arg.end(), 0);
  map<char, int> hand;
  hand['G'] = 0;
  hand['C'] = 1;
  hand['P'] = 2;
  auto calc_result = [&](char x, char y) -> int {
    if(x == y) return 0;
    if((hand[x] + 1) % 3 == hand[y]) {
      return 1;
    } else {
      return -1;
    }
  };
  for(int j = 0; j < m; j++) {
    for(int i = 0; i < n2; i += 2) {
      int x = arg[i], y = arg[i + 1];
      int res = calc_result(a[x][j], a[y][j]);
      if(res == 0) continue;
      if(res == -1) {
        wins[y]++;
      } else {
        wins[x]++;
      }
    }
    sort(arg.begin(), arg.end(), [&](int i, int j) {
      if(wins[i] != wins[j]) { return wins[i] > wins[j]; }
      return i < j;
    });
  }
  for(int i = 0; i < n2; i++) { cout << arg[i] + 1 << " \n"[i == n2 - 1]; }
}
