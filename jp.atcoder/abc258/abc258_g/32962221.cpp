#include <bits/stdc++.h>

using namespace std;

template <int N>
class bit_array {
  constexpr static int K = 6;
  constexpr static int M = (1 << K) - 1;

  constexpr static int n = (N + M) >> K;
  array<ulong, n> d;
  using Self = bit_array;

public:
  // bit_array() : bit_array(0) {}

  // bit_array(int size) : d((size + M) >> K) {}

  auto operator[](int i) -> int { return d[i >> K] >> (i & M) & 1; }

  void set(int i, int value) {
    if ((*this)[i] != value) flip(i);
  }

  void flip(int i) { d[i >> K] ^= 1ul << (i & M); }

  auto operator&(const Self& rhs) -> Self {
    Self res(*this);
    for (int i = 0; i < n; i++) {
      res.d[i] &= rhs.d[i];
    }
    return res;
  }

  auto popcount() -> int {
    int cnt = 0;
    for (auto& x : d) {
      cnt += __builtin_popcountll(x);
    }
    return cnt;
  }
};

auto main() -> int {
  using namespace std;
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<bit_array<3000>> a(n);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      char e;
      cin >> e;
      if (e == '1') a[i].set(j, 1);
    }
  }

  long res = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (a[i][j]) res += (a[i] & a[j]).popcount();
    }
  }
  cout << res / 3 << endl;
}
