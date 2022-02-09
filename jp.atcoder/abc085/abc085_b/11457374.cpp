#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<bool> exist(101);
  for (int i = 0; i < n; i++) {
    int d;
    cin >> d;
    exist[d] = true;
  }

  int res = 0;
  for (int i = 0; i < 101; i++) {
    res += exist[i];
  }
  cout << res << '\n';
  return 0;
}
