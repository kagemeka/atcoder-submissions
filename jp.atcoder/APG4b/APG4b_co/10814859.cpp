#include <bits/stdc++.h>
using namespace std;

int main() {
  int p;
  cin >> p;

  string text;
  if (p == 2) {
    cin >> text;
  }

  int price, n;
  cin >> price >> n;

  if (p == 2) {
    cout << text + "!" << endl;
  }
  cout << price * n << endl;

}
