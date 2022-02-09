#include <bits/stdc++.h>
using namespace std;

int INF = 1001001001;
int n, A, B, C;
vector<int> l(8);

int cost(int a, int b, int c, int cnt, int i) {
  if (i == n) {
    if (!(a && b && c)) return INF;
    return abs(A - a) + abs(B - b) + abs(C - c) + 10 * (cnt - 3);
  }
  vector<int> cand = {cost(a, b, c, cnt, i+1),
                      cost(a+l[i], b, c, cnt+1, i+1),
                      cost(a, b+l[i], c, cnt+1, i+1),
                      cost(a, b, c+l[i], cnt+1, i+1)};
  return *min_element(cand.begin(), cand.end());
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cin >> n >> A >> B >> C;
  for (int i = 0; i < n; i++) cin >> l[i];
  cout << cost(0, 0, 0, 0, 0) << '\n';
  return 0;
}
