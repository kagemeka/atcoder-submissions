#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> c(3);
  for (int i = 0; i < 3; i++) {
    cin >> c[i];
  }
  sort(c.begin(), c.end());
  cout << c[0] + c[1] << endl;
  return 0;
}
