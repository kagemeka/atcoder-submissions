#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, l;
  cin >> n >> l;
  int s = (l * 2 + n - 1) * n / 2;
  if (l < -(n - 1)) s -= l + (n - 1);
  else if (l > 0) s -= l;
  cout << s << '\n';
  return 0;
}
