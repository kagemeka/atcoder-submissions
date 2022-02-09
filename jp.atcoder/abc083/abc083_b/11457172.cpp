#include <bits/stdc++.h>
using namespace std;

int sum_d(int n) {
  int tot = 0;
  while (n) {
    tot += n % 10;
    n /= 10;
  }
  return tot;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a, b;
  cin >> n >> a >> b;

  int tot = 0;
  for (int i = 1; i <= n; i++) {
    int s = sum_d(i);
    if (s >= a && s <= b) tot += i;
  }
  cout << tot << '\n';
  return 0;
}
