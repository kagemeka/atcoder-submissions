#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> b(3, vector<int>(3));
vector<vector<int>> c(3, vector<int>(3));

vector<int> optimize(vector<vector<int>> board, int moves) {
  if (moves == 9) {
    int tot_1 = 0, tot_2 = 0;
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 3; j++) {
        (board[i][j] == board[i+1][j]) ? tot_1 += b[i][j] : tot_2 += b[i][j];
      }
    }
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 2; j++) {
        (board[i][j] == board[i][j+1]) ? tot_1 += c[i][j] : tot_2 += c[i][j];
      }
    }
    return {tot_1, tot_2};
  }

  vector<vector<int>> results;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (!board[i][j]) {
        vector<vector<int>> nxt_board = board;
        nxt_board[i][j] = ((moves + 1) & 1 ^ 1) + 1;
        vector<int> res = optimize(nxt_board, moves+1);
        results.push_back(res);
      }
    }
  }
  sort(results.begin(), results.end());
  vector<int> res = (moves & 1) ? results[0] : results[results.size()-1];
  return res;
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
  vector<int> res = optimize(board, 0);
  for (int &r : res) {
    cout << r << '\n';
  }

  return 0;
}
