#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n = 5;
  int a;
  int s = 0;
  int d = 0;
  for (int i = 0; i < n; i++) {
    cin >> a;
    int tmp = (a + 9) / 10 * 10;
    d = max(d, tmp - a);
    s += tmp;
  }
  cout << s - d << '\n';
  return 0;
}
