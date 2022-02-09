#include <iostream>
using namespace std;


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m; cin >> n >> m;

  int x = 0, y = 0, z = 0;
  if (m & 1) {
    m -= 3;
    n--;
    y = 1;
  }
  z = m / 2 - n;
  x = n - z;
  if (x < 0 or y < 0 or z < 0) {
    x = -1, y = -1, z = -1;
  }
  cout << x << ' ' << y << ' ' << z << '\n';
}
