#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int cnt = 0;

  for (int i = a; i <= b; i++) {
    string k = to_string(i);
    bool flag = true;
    for (int j = 0; j < 2; j++) {
      if (k[j] != k[4-j]) {
        flag = false;
        break;
      }
    }
    if (flag) {
      cnt++;
    }
  }
  cout << cnt << endl;
}
