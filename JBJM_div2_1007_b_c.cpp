#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 1e5;
vector<vector<int>> dp(MAX);

bool isPerfectSquare(long long num) {
    long long sq = sqrt(num);
    return sq * sq == num;
}

long long getSum(const vector<int>& p) {
    long long sum = 0;
    for (int num : p) {
        sum += num;
    }
    return sum;
}

bool isPerfectPermutation(const vector<int>& p) {
    long long prefixSum = 0;
    for (int num : p) {
        prefixSum += num;
        if (isPerfectSquare(prefixSum)) {
            return false;
        }
    }
    return true;
}

void precompute() {
    dp[1] = {-1};
    dp[2] = {2, 1};

    for (int n = 3; n < MAX; n++) {
        long long totalSum = (1LL * n * (n + 1)) / 2;
        if (isPerfectSquare(totalSum)) {
            dp[n] = {-1};
            continue;
        }
        if (dp[n - 1][0] != -1 && !isPerfectSquare(totalSum - n)) {
            dp[n] = dp[n - 1];
            dp[n].push_back(n);
        } else {
            dp[n] = dp[n - 2];
            dp[n].push_back(n);
            dp[n].push_back(n - 1);
        }
    }
}

void solve() {
    int t;
    cin >> t;
    precompute();
    while (t--) {
        int n;
        cin >> n;
        if (dp[n][0] == -1) {
            cout << "-1\n";
        } else {
            for (int num : dp[n]) {
                cout << num << " ";
            }
            cout << "\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}
