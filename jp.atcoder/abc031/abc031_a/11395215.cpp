#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, d;
  cin >> a >> d;
  (a <= d) ? a++ : d++;
  cout << a * d << endl;
  return 0;
}
