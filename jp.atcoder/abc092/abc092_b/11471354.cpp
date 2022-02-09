#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, d, x;
  cin >> n >> d >> x;
  int tot = x;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    tot += (d - 1) / a + 1;
  }
  cout << tot << '\n';
  return 0;
}
