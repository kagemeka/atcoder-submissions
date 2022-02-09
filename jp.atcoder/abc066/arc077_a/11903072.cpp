#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  deque<int> b;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    (i & 1) ? b.push_front(a) : b.push_back(a);
  }
  if (n & 1) reverse(b.begin(), b.end());
  for (int i = 0; i < n; i++) {
    char tail = (i == n - 1) ? '\n' : ' ';
    cout << b[i] << tail;
  }
  return 0;
}
