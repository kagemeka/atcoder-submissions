#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> res;
  for (int i = 0; i < 4; i++) {
    if (n >> i & 1) res.push_back(i);
  }
  cout << res.size() << endl;
  for (auto r : res) cout << pow(2, r) << endl;
  return 0;
}
