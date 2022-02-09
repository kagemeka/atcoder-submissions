#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  int a, b = 0, c;
  if (m & 1) {
    n--;
    m -= 3;
    b++;
  }
  if (m < 2 * n || m > 4 * n) {
    cout << "-1 -1 -1" << '\n';
  } else {
    m /= 2;
    c = m - n;
    a = n - c;
    printf("%d %d %d\n", a, b, c);
  }
  return 0;
}
