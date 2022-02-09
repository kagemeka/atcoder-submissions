#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> p(n);
  for (int i = 0; i < n; i++) {cin >> p[i];}
  vector<bool> res(n-1);
  for (int i = 0; i < n - 1; i++) {
    res[i] = p[i+1] > p[i];
  }
  int cnt = 0;
  for (int i = 0; i < n - 2; i++) {
    cnt += res[i+1] == res[i];
  }
  cout << cnt << '\n';
  return 0;
}
