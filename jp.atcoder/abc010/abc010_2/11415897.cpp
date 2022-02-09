#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int cnt = 0;
  int a;
  for (int i = 0; i < n; i++) {
    cin >> a;
    if (a % 3 == 2) {
      a--;
      cnt++;
    }
    if (a % 2 == 0) {
      a--;
      cnt++;
    }
  }
  cout << cnt << '\n';
  return 0;
}
