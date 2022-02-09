#include <bits/stdc++.h>
using namespace std;

int MOD = 10007;

vector<int> tribonacci() {
  vector<int> table(100100);
  table[0] = 0; table[1] = 0; table[2] = 1;
  for (int i = 3; i < table.size(); i++) {
    table[i] = table[i-2] + table[i-1] + table[i-3];
    table[i] %= MOD;
  }
  return table;
}

int main() {
  int n;
  cin >> n;
  vector<int> table = tribonacci();
  cout << table[n-1] << endl;
  return 0;
}
