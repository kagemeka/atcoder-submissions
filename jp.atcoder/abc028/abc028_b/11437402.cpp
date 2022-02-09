#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string cand = "ABCDEF";
  map<char, int> res;

  string s;
  cin >> s;
  for (char &c : s) {res[c]++;}
  for (char &c : cand) {cout << res[c];}
  cout << '\n';
  return 0;
}
