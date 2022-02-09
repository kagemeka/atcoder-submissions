#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<char>> res(n+1, vector<char>(n+1, '-'));
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    res[a][b] = 'o';
    res[b][a] = 'x';
  }
  for (int i = 1; i < n+1; i++) {
    for (int j = 1; j < n+1; j++) {
      cout << res[i][j] << " ";
    }
    cout << endl;
  }
  return 0;
}
