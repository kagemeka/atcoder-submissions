#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> t(3);
  for (int i = 0; i < 3; i++) {
    cin >> t[i];
  }
  cout << accumulate(t.begin(), t.end(), 0) - *max_element(t.begin(), t.end()) << endl;
  return 0;
}
