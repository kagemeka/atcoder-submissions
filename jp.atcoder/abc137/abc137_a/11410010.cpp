#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  vector<int> c = {a+b, a-b, a*b};
  cout << *max_element(c.begin(), c.end()) << endl;
  return 0;
}
