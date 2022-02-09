#include <bits/stdc++.h>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n = 4;

  vector<vector<char>> table(n, vector<char>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> table[i][j];
    }
  }
  for (int i = n - 1; i > -1; i--) {
    for (int j = n - 1; j > -1; j--) {
      cout << table[i][j];
      char tail = (j > 0) ? ' ' : '\n';
      cout << tail;
    }
  }
  return 0;
}
