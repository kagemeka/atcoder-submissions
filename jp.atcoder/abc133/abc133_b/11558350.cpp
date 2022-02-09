#include <bits/stdc++.h>
using namespace std;

bool dist_is_int(vector<int> &a, vector<int> &b, int n) {
  double d = 0;
  for (int i = 0; i < n; i++) {
    d += (a[i] - b[i]) * (a[i] - b[i]);
  }
  d = sqrt(d);
  return d == floor(d);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, d;
  cin >> n >> d;
  vector<vector<int>> x(n, vector<int>(d));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < d; j++) {
      cin >> x[i][j];
    }
  }
  int cnt = 0;
  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      cnt += dist_is_int(x[i], x[j], d);
    }
  }
  cout << cnt << '\n';
  return 0;
}
