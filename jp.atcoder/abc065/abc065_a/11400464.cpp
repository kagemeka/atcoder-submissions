#include <bits/stdc++.h>
using namespace std;

int main() {
  int x, a, b;
  cin >> x >> a >> b;
  int c = -a + b;
  string ans;
  if (c <= 0) {
    ans = "delicious";
  } else if (c <= x) {
    ans = "safe";
  } else {
    ans = "dangerous";
  }
  cout << ans << endl;
  return 0;

}
