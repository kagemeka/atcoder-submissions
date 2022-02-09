#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> b(2, vector<int>(3));
vector<vector<int>> c(3, vector<int>(2));
map<vector<vector<int>>, pair<int, int>> situation;

pair<int, int> dfs(vector<vector<int>> board, int moves) {
  if (situation.find(board) != situation.end()) {return situation[board];}
  if (moves == 9) {
    int tot1 = 0, tot2 = 0;
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        if (i < 2) {
          (board[i][j] == board[i+1][j]) ? tot1 += b[i][j] : tot2 += b[i][j];
        }
        if (j < 2) {
          (board[i][j] == board[i][j+1]) ? tot1 += c[i][j] : tot2 += c[i][j];
        }
      }
    }
    situation[board] = pair<int, int>(tot1, tot2);
    return situation[board];
  }
  vector<pair<int, int>> results;
  int p = (moves & 1) + 1;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (!board[i][j]) {
        auto nxt_board = board;
        nxt_board[i][j] = p;
        results.push_back(dfs(nxt_board, moves+1));
      }
    }
  }
  sort(results.begin(), results.end());
  situation[board] = (p == 2) ? results[0] : results[8-moves];;
  return situation[board];
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
      cin >> b[i][j];
    }
  }
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 2; j++) {
      cin >> c[i][j];
    }
  }
  vector<vector<int>> board(3, vector<int>(3));
  auto res = dfs(board, 0);
  cout << res.first << '\n';
  cout << res.second << '\n';
  return 0;
}
