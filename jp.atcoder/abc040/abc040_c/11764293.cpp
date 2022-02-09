#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> h(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> h[i];
  h[0] = h[1];
  vector<int> cost(n + 1);
  for (int i = 2; i < n + 1; i++) {
    cost[i] = min(cost[i-1] + abs(h[i] - h[i-1]), cost[i-2] + abs(h[i] - h[i-2]));
  }
  cout << cost[n] << '\n';
  return 0;
}
