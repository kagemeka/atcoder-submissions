#include <bits/stdc++.h>
using namespace std;

int max(vector<int> &vec) {
  int res = -100;
  for (int &v : vec) {
    res = max(res, v);
  }
  return res;
}

int main() {
  int a, b;
  cin >> a >> b;
  vector<int> c = {a + b, a - b, a * b};

  cout << max(c) << endl;
  return 0;
}
