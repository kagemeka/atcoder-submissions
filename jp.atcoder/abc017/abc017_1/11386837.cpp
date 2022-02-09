#include <bits/stdc++.h>
using namespace std;

int main() {
  int res = 0;
  int s, e;
  for (int i = 0; i < 3; i++) {
    cin >> s >> e;
    res += s / 10 * e;
  }
  cout << res << endl;
  return 0;
}
