#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<pair<int, int>> a(3);
  for (int i = 0; i < 3; i++) {
    int x;
    cin >> x;
    a[i] = (make_pair(x, i));
  }
  sort(a.begin(), a.end(), greater<pair<int, int>>());

  vector<int> res(3);
  for (int i = 0; i < 3; i++) {
    res[a[i].second] = i + 1;
  }

  for (int r : res) {
    cout << r << endl;
  }
  return 0;
}
