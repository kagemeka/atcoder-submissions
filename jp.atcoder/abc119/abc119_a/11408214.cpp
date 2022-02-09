#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  string b = "2019/04/30";
  string ans = (s <= b) ? "Heisei" : "TBD";
  cout << ans << endl;
  return 0;
}
