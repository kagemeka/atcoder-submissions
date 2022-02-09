#include <bits/stdc++.h>
using namespace std;

int main() {
  set<int> color;
  for (int i = 0; i < 3; i++) {
    int c;
    cin >> c;
    color.insert(c);
  }
  cout << color.size() << endl;
  return 0;
}
