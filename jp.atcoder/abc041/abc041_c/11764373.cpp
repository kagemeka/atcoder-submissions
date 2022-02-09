#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<pair<int, int>> a(n);
  for (int i = 0; i < n; i++) {
    int h;
    cin >> h;
    a[i] = pair<int, int>(h, i + 1);
  }
  sort(a.begin(), a.end(), greater<pair<int, int>>());
  for (int i = 0; i < n; i++) {
    cout << a[i].second << '\n';
  }
  return 0;

}
