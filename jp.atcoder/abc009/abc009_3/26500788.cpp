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
    char c = s[i];
    int min_cost = 0;
    int idx = -1;
    for (int j = i + 1; j < n; j++) {
      if (s[j] > c) continue;
      int cost = swap_cost[i] + swap_cost[j];
      if (cost > k || s[j] == c && cost > min_cost) continue;
      c = s[j];
      min_cost = cost;
      idx = j;
    }
    if (idx == -1) continue;
    swap(s[i], s[idx]);
    k -= min_cost;
    swap_cost[i] = swap_cost[idx] = 0;
  }
  cout << s << '\n';

}
