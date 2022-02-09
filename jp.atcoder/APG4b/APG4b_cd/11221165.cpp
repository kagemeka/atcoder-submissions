#include <bits/stdc++.h>
using namespace std;

int correct(int n, int &c, int &w, vector<vector<int>> &table) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (table[i][j] == (i + 1) * (j + 1)) {
        c++;
      } else {
        w++;
        table[i][j] = (i + 1) * (j + 1);
      }
    }
  }
}

int main() {
  int n = 9;
  vector<vector<int>> table(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> table[i][j];
    }
  }
  int correct_cnt = 0, wrong_cnt = 0;
  correct(n, correct_cnt, wrong_cnt, table);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << table[i][j];
      string tail = (j == n - 1) ? "\n" : " ";
      cout << tail;
    }
  }
  cout << correct_cnt << endl << wrong_cnt << endl;
  return 0;
}
