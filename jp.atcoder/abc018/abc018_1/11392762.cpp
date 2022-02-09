#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> enumerate(vector<int> &vec) {
  int n = vec.size();
  vector<pair<int, int>> nvec(n);
  for (int i = 0; i < n; i++) {
    nvec[i] = make_pair(i, vec[i]);
  }
  return nvec;
}

bool descending_second(pair<int, int> &a, pair<int, int> &b) {
  if (a.second == b.second) {
    return a.first > b.first;
  } else {
    return a.second > b.second;
  }
}

int main() {
  vector<int> a(3);
  for (int i = 0; i < 3; i++) {
    cin >> a[i];
  }

  vector<pair<int, int>> b = enumerate(a);
  sort(b.begin(), b.end(), descending_second);

  vector<int> res(3);
  for (int i = 0; i < 3; i++) {
    res[b[i].first] = i + 1;
  }

  for (auto r : res) {
    cout << r << endl;
  }
  return 0;
}
