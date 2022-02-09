#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<vector<int>> x(2, vector<int>(2));
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
      cin >> x[i][j];
    }
  }

  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
      if (x[0][i] == x[1][j]) {
        cout << "YES" << '\n';
        return 0;
      }
    }
  }
  cout << "NO" << '\n';
  return 0;
}
