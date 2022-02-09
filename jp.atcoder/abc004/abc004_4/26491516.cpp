#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int r, g, b;
  cin >> r >> g >> b;
  int k = 1 << 10;
  vector<int> from(k);
  for (int i = 1; i < r + 1; i++) from[i] = 400;
  for (int i = r + 1; i < r + g + 1; i++) from[i] = 500;
  for (int i = r + g + 1; i < k; i++) from[i] = 600;

  int inf = 1 << 30;
  vector<int> dp(k, inf);
  dp[0] = 0;
  for (int i = 0; i < k; i++) {
    for (int j = k - 1; j > 0; j--) {
      dp[j] = min(dp[j], dp[j - 1] + abs(i - from[j]));
    }
  }
  cout << dp[r + g + b] << '\n';

}
