#include <bits/stdc++.h>
using namespace std;

int main() {
  unordered_set<int> a;
  for (int i = 0; i < 2; i++) {
    int b;
    cin >> b;
    a.insert(b);
  }
  for (int i = 1; i <= 3; i++) {
    if (a.find(i) == a.end()) {
      cout << i << endl;
      return 0;
    }
  }
}
