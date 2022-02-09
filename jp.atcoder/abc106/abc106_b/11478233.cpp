#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  vector<int> cand = {135, 189, 105, 165, 195};
  sort(cand.begin(), cand.end());

  int n;
  cin >> n;
  cout << upper_bound(cand.begin(), cand.end(), n) - cand.begin() << '\n';
  return 0;
}
