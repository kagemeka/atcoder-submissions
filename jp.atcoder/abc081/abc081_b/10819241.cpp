#include <bits/stdc++.h>
using namespace std;

int main() {
  int n; cin >> n;

  int res = 30;
  for (int i = 0; i < n; i ++ ) {
    int a; cin >> a;
    int cnt = 0;
    while (a % 2 == 0) {
      a /= 2;
      cnt++;
    }
    res = min(res, cnt);
  }
  cout << res << endl;
}
