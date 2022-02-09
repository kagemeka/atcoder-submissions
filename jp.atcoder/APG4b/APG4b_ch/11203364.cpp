#include <bits/stdc++.h>
using namespace std;

int sum(vector<int> a) {
  int tot = 0;
  for (int i: a) {
    tot += i;
  }
  return tot;
}

int main() {
  int n;
  cin >> n;
  vector<vector<int>> res(3, vector<int>(n));
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < n; j++) {
      cin >> res[i][j];
    }
  }

  long long ans = 1;
  for (int i = 0; i < 3; i++) {
    ans *= sum(res[i]);
  }
  cout << ans << endl;
  return 0;
}
