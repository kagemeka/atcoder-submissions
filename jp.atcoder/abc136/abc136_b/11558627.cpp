#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int l = floor(log10(n)) + 1;
  int cnt = 0;
  for (int i = 0; i < l; i += 2) {
    if (i == l - 1) {
      cnt += n - pow(10, i) + 1;
    } else {
      cnt += 9 * pow(10, i);
    }
  }
  cout << cnt << '\n';
  return 0;
}
