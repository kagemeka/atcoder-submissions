#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  deque<int> que;
  for(auto& x: a) que.push_back(x);
  int cnt = 0;
  while(que.size() > 1) {
    int x = que.back();
    que.pop_back();
    x %= que.front();
    if(x > 0) que.push_front(x);
    cnt++;
  }
  cout << cnt << endl;
}
