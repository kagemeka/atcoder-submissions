#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<int> a(3);
  for (int i = 0; i < 3; i++) cin >> a[i];
  swap(a[0], a[1]);
  swap(a[0], a[2]);
  for (int i = 0; i < 3; i++) {
    cout << a[i];
    char tail = (i == 2) ? '\n' : ' ';
    cout << tail;
  }
  return 0;
}
