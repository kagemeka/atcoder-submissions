#include <bits/stdc++.h>

using namespace std;


int main() {
  int n = 4;
  set<string> a;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    a.insert(s);
  }
  vector<string> t = {
    "H",
    "2B",
    "3B",
    "HR",
  };
  bool ok = true;
  for (auto x: t) {
    ok &= a.count(x);
  }
  cout <<
  (ok ? "Yes" : "No")
  << '\n';
}
