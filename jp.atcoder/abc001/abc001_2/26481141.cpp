#include <bits/stdc++.h>
using namespace std;


int main() {
  int m;
  cin >> m;
  int v;
  if (m < 100) {
    v = 0;
  } else if (m <= 5000) {
    v = m * 10 / 1000;
  } else if (m <= 30000) {
    v = m / 1000 + 50;
  } else if (m <= 70000) {
    v = (m / 1000 - 30) / 5 + 80;
  } else {
    v = 89;
  }
  printf("%02d\n", v);
}
