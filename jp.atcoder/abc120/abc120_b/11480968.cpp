#include <bits/stdc++.h>
using namespace std;

vector<int> divisor(int n) {
  vector<int> res;
  for (int i = 1; i < floor(sqrt(n)) + 1; i++) {
    if (n % i) continue;
    int j = n / i;
    res.emplace_back(i);
    res.emplace_back(j);
  }
  sort(res.begin(), res.end());
  return res;
}

int gcd(int a, int b) {
  while (b) {
    int c = a % b;
    a = b;
    b = c;
  }
  return abs(a);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, k;
  cin >> a >> b >> k;
  vector<int> cand = divisor(gcd(a, b));
  cout << cand[cand.size()-k] << '\n';
  return 0;
}
