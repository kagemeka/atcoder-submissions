#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  string a;
  if (n < 60) {
    a = "Bad";
  } else if (n < 90) {
    a = "Good";
  } else if (n < 100) {
    a = "Great";
  } else {
    a = "Perfect";
  }
  cout << a << endl;
  return 0;
}
