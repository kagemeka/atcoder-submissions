#include <iostream>
#include <vector>
using namespace std;


long long prohibited_count(long long n) {
  string m = to_string(n);
  long long dp[2];
  dp[0] = 1, dp[1] = 0;
  for (const char &c : m) {
    int d = c - '0';
    dp[1] = dp[1] * 8 + dp[0] * (d - (d > 4));
    if (d == 4 or d == 9) dp[0] = 0;
  }
  return n + 1 - dp[0] - dp[1];
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  long long a, b;
  cin >> a >> b;
  cout << prohibited_count(b) - prohibited_count(a - 1) << '\n';
}
