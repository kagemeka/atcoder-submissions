#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, w;
  cin >> h >> w;
  vector<vector<char>> grid(h+2, vector<char>(w+2,'#'));

  for (int i = 1; i < h+1; i++) {
    for (int j = 1; j < w+1; j++) {
      cin >> grid[i][j];
    }
  }

  for (int i = 0; i < h+2; i++) {
    for (int j = 0; j < w+2; j++) {
      cout << grid[i][j];
    }
    cout << endl;
  }
}
