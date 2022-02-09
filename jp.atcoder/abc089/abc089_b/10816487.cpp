#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n; i++) {
    string c;
    cin >> c;
    if (c == "Y") {
      cout << "Four" << endl;
      return(0);
    }
  }
  cout << "Three" << endl;
}
