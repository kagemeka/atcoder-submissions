#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> t(3);
  int q, r;
  for (int i = 0; i < 3; i++) {
    int p = pow(60, 2 - i);
    q = n / p;
    r = n % p;
    t[i] = q;
    n = r;
  }

  for (int i = 0; i < 3; i++) {
    string x = to_string(t[i]);
    if (t[i] < 10) x = '0' + x;
    cout << x;
    char tail = (i < 2) ? ':' : '\n';
    cout << tail;
  }
  return 0;
}
