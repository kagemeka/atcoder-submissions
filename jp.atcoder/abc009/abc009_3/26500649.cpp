#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  string s;
  cin >> n >> k >> s;

  vector<int> swap_cost(n, 1);
  for (int i = 0; i < n; i++) {
    char c = ' ';
    int min_cost = 1 << 30;
    int idx = -1;
    for (int j = i + 1; j < n; j++) {
      if (s[j] >= s[i]) continue;
      int cost = swap_cost[i] + swap_cost[j];
      if (cost > k or cost > min_cost) continue;
      c = s[j];
      if (cost < min_cost) min_cost = cost;
      idx = j;
    }
    if (idx == -1) continue;
    swap(s[i], s[idx]);
  }
  cout << s << '\n';

}
