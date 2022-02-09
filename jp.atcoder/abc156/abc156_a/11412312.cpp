#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, r;
  cin >> n >> r;
  r += 100 * max(10 - n, 0);
  cout << r << endl;
  return 0;

}
