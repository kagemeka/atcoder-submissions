#include <bits/stdc++.h>
using namespace std;


template<typename T>
struct Matrix: public vector<T>
{

public:

using Mat = vector<vector<T>>;

Matrix() {}

Matrix(
  const int& h,
  const int& w) {
  m = Mat(h, vector<T>(w));
}

Matrix(const int& n) {
  m = Mat(n, vector<T>(n));
}

vector<T>& operator[](
  int i)
{
  return m[i];
}

constexpr int size() const
{
  return (int)m.size();
}


T bitwise_dot_compute(
  Matrix &other,
  const int& i, const int& j
) {
  int n = (int)m[0].size();
  T x = 0;
  for (int k = 0; k < n; k++)
  {
    x ^= m[i][k] & other[k][j];
  }
  return x;
}

Matrix bitwise_dot(
  Matrix& other
) {
  int h = m.size();
  int w = other[0].size();
  assert(
    m[0].size()==other.m.size()
  );
  Matrix a(h, w);
  for (int i = 0; i < h; i++)
  {
    for (int j = 0; j < w; j++)
    {
      a[i][j] =
        bitwise_dot_compute(
        other, i, j
      );
    }
  }
  return a;
}


Matrix bitwise_identity(int n)
{
  Matrix e(n);
  T inf =
    numeric_limits<T>::max();
  for (int i = 0; i < n; i++)
  {
    e[i][i] = inf;
  }
  return e;
}


Matrix bitwise_pow(long long n)
{
  if (!n)
  {
    return bitwise_identity(
      (int)m.size()
    );
  }
  Matrix a = bitwise_pow(n>>1);
  a = a.bitwise_dot(a);
  if (n&1)
  {
    a = a.bitwise_dot(*this);
  }
  return a;
}


private:

Mat m;

};

class Solver {

private:

int k, m;
Matrix<uint> a;
vector<uint> c;

void prepare() {
  cin >> k >> m;
  a = Matrix<uint>(k, 1);

  c = vector<uint>(k);
  for (int i = 0; i < k; i++)
  {
    cin >> a[k-i-1][0];
  }

  for (int i = 0; i < k; i++)
  {
    cin >> c[i];
  }

}


void solve() {
  Matrix<uint> d(k);
  d[0] = c;

  int inf =
    numeric_limits<uint>::max();
  for (int i = 1; i < k; i++)
  {
    d[i][i-1] = inf;
  }


  if (m <= k) {
    // cout << a[m-1][0] << '\n';
    cout << a[k-m][0] << '\n';

    return;
  }

  reverse(a.begin(), a.end());

  d = d.bitwise_pow(m - k);

  a = d.bitwise_dot(a);
  cout << a[0][0] << '\n';

}

public:

void run() {
  prepare();
  solve();
}

};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    Solver solver;
    solver.run();
  }

  return 0;
}
