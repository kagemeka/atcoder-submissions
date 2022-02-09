#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, a;
  cin >> n >> a;
  int r = n % 500;

  if (r <= a) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
