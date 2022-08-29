#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  stack<int> st;
  while(n--) {
    cout << st.size() << '\n';
    int x;
    cin >> x;
    while(st.size() && st.top() < x) st.pop();
    st.push(x);
  }
}
