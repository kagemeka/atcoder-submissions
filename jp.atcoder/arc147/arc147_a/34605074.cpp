#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  int mn = a[0];
  priority_queue<int> que;
  for(int i = 1; i < n; i++) que.push(a[i]);
  int cnt = 0;
  while(que.size()) {
    cnt++;
    int x = que.top();
    que.pop();
    x %= mn;
    if(x == 0) continue;
    swap(x, mn);
    que.push(x);
  }
  cout << cnt << endl;
}
