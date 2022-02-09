#include <bits/stdc++.h>
using namespace std;

int main() {
  string n;
  cin >> n;
  set<int> s;
  for (char c : n) s.insert(c);
  string ans = (s.size() == 1) ? "SAME" : "DIFFERENT";
  cout << ans << endl;
  return 0;

}
