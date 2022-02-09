#include <bits/stdc++.h>
using namespace std;

int main() {
  string n;
  cin >> n;
  for (int i = 0; i < n.size(); i++) {
    n[i] = (n[i] == '1') ? '9' : '1';
  }
  cout << n << endl;
  return 0;
}
