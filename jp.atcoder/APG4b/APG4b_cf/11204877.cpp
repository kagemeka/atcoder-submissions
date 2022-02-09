#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, s;
  cin >> n >> s;
  vector<int> a(n), p(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  for (int i = 0; i < n; i++) {
    cin >> p[i];
  }

  int cnt = 0;
  for (int i : a) {
    for (int j : p) {
      (i + j == s) ? cnt++ : false;
    }
  }
  cout << cnt << endl;
  return 0;
}
