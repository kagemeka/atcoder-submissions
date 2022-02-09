#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  string ans = (a <= 8 && b <= 8) ? "Yay!" : ":(";
  cout << ans << endl;
  return 0;
}
