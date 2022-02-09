#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  long long k;
  cin >> n >> k;
  vector<vector<int>> ab(n, vector<int>(2));
  for (int i = 0; i < n; i++) {
    cin >> ab[i][0];
    cin >> ab[i][1];
  }
  sort(ab.begin(), ab.end());
  long long cnt = 0;
  for (auto &p : ab) {
    cnt += p[1];
    if (cnt >= k) {
      cout << p[0] << '\n';
      return 0;
    }
  }
}
