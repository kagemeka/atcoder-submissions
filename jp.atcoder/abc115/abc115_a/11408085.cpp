#include <bits/stdc++.h>
using namespace std;

int main() {
  int d;
  cin >> d;
  string ans = "Christmas";
  for (int i = 0; i < 25 - d; i++) {
    ans += " Eve";
  }
  cout << ans << endl;
  return 0;
}
