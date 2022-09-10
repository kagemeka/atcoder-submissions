#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  set<int> st;
  for(int i = 0; i < 5; i++) {
    int x;
    cin >> x;
    st.insert(x);
  }
  cout << st.size() << endl;
}
