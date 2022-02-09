#include <bits/stdc++.h>
using namespace std;

int main() {
  set<int> res;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    res.insert(a);
  }
  cout << res.size() << endl;

  return 0;
}
