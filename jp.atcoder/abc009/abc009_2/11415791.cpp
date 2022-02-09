#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  set<int> a;
  int b;
  for (int i = 0; i < n; i++) {
    cin >> b;
    a.insert(b);
  }

  vector<int> t(a.begin(), a.end());

  cout << t[t.size()-2] << '\n';
  return 0;
}
