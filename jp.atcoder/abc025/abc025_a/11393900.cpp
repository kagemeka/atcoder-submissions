#include <bits/stdc++.h>
using namespace std;

vector<string> dfs(vector<string> s, string &cand, int n) {
  if (s[0].size() == n) return s;
  vector<string> ns;
  for (string t : s) {
    for (char c : cand) {
      ns.push_back(t + c);
    }
  }
  return dfs(ns, cand, n);
}

int main() {
  string s;
  int n;
  cin >> s >> n;

  vector<string> res = dfs({""}, s, 2);
  cout << res[n-1] << endl;
  return 0;
}
