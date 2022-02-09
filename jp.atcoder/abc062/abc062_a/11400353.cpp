#include <bits/stdc++.h>
using namespace std;

vector<int> group = {0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0};

int main() {
  int x, y;
  cin >> x >> y;
  string ans = (group[x-1] == group[y-1]) ? "Yes" : "No";
  cout << ans << endl;
  return 0;
}
