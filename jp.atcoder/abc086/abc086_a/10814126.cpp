#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  int p = a * b;
  if (p & 1) {
    cout << "Odd" << endl;
  } else {
    cout << "Even" << endl;
  }
}
