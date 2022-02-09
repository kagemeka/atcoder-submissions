#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int c = 31;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    int tmp = 0;
    while (a % 2 == 0) {
      a /= 2;
      tmp++;
    }
    c = min(c, tmp);
  }
  cout << c << '\n';
  return 0;
}
