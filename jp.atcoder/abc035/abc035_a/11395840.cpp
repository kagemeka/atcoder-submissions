#include <bits/stdc++.h>
using namespace std;

int main() {
  int w, h;
  cin >> w >> h;
  string ans = (w * 3 == h * 4) ? "4:3" : "16:9";
  cout << ans << endl;
  return 0;
}
