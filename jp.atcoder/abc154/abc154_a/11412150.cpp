#include <bits/stdc++.h>
using namespace std;

int main() {
  string s, t;
  int a, b;
  string u;
  cin >> s >> t >> a >> b >> u;
  map<string, int> res;
  res[s] = a;
  res[t] = b;
  res[u]--;
  cout << res[s] << " " << res[t] << endl;
  return 0;
}
