#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<string> grid(n);
  for (int i = 0; i < n; i++) {
    cin >> grid[i];
  }

  for (int j = 0; j < n; j++) {
    for (int i = n-1; i > -1; i--) {
      cout << grid[i][j];
    }
    cout << '\n';
  }
  return 0;
}
