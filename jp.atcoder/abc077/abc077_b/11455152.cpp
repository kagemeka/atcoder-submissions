#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  int m = floor(sqrt(n));
  m *= m;
  cout << m << '\n';
  return 0;
}
