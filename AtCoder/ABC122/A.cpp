#include <bits/stdc++.h>
using namespace std;

int main() {
  char b; cin >> b;
  cout << (b == 'A' ? 'T' : (b == 'T' ? 'A' : (b == 'G' ? 'C' : 'G'))) << endl;
}
