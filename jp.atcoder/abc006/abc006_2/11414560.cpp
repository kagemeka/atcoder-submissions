#include <bits/stdc++.h>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int MOD = 1e4 + 7;
  vector<int> tribonacci(1001001);
  tribonacci[0] = 0;
  tribonacci[1] = 0;
  tribonacci[2] = 1;

  for (int i = 3; i < 1001001; i++) {
    tribonacci[i] = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3];
    tribonacci[i] %= MOD;
  }

  int n;
  cin >> n;
  cout << tribonacci[n-1] << endl;
  return 0;
}
