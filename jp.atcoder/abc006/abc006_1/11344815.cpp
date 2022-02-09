#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  string ans = "NO";
  if (!(n % 3)) ans = "YES";
  while (n) {
    if (n % 10 == 3) {
      ans = "YES";
      break;
    }
    n /= 10;
  }
  cout << ans << endl;
  return 0;
}
