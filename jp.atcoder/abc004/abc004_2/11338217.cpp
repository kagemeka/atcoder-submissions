#include <bits/stdc++.h>
using namespace std;

int main() {
  int n = 4;
  vector<vector<char>> c(n, vector<char>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> c[i][j];
    }
  }

  for (int i = n - 1; i > -1; i--) {
    for (int j = n - 1; j > -1; j--) {
      cout << c[i][j];
      if (j == 0) {
        cout << endl;
      } else {
        cout << " ";
      }
    }
  }
  return 0;
}
