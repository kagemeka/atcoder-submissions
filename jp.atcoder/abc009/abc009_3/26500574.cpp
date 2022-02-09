#include <iostream>
#include <queue>
#include <string>
#include <tuple>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  string s;
  cin >> n >> k >> s;

  using tup = tuple<char, int, int>;
  vector<int> swap_cost(n, 1);
  for (int i = 0; i < n; i++) {
    priority_queue<tup, vector<tup>, greater<tup>> que;
    for (int j = i + 1; j < n; j++) {
      if (s[j] >= s[i]) continue;
      int cost = swap_cost[i] + swap_cost[j];
      if (cost > k) continue;
      que.emplace(s[j], cost, -j);
    }
    if (que.empty()) continue;
    char c; int cost, j;
    tie(c, cost, j) = que.top();
    j = -j;
    swap(s[i], s[j]);
    k -= cost;
    swap_cost[i] = swap_cost[j] = 0;
  }
  cout << s << '\n';

}
