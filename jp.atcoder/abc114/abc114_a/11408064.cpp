#include <bits/stdc++.h>
using namespace std;

string cand = "753";

int main() {
  char x;
  cin >> x;
  string ans = (cand.find(x) != string::npos) ? "YES" : "NO";
  cout << ans << endl;
  return 0;
}
