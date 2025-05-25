#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>
using namespace std;

string findOrder(string dict[], int N, int K) {
    unordered_map<char, vector<char>> adj;
    unordered_map<char, int> deg;
    vector<char> vec;

    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < min(dict[i].size(), dict[i + 1].size()); j++) {
            if (dict[i][j] != dict[i + 1][j]) {
                adj[dict[i][j]].push_back(dict[i + 1][j]);
                deg[dict[i + 1][j]]++;
                break;  // break to only consider first different character
            }
        }
    }

    //Initialize degrees for all chars present
    for (int i = 0; i < N; i++) {
        for (char c : dict[i]) {
            if (deg.find(c) == deg.end()) {
                deg[c] = 0;
            }
        }
    }

    queue<char> q;
    for (auto& pair : deg) {
        if (pair.second == 0) {
            q.push(pair.first);
        }
    }

    while (!q.empty()) {
        char t = q.front();
        q.pop();
        vec.push_back(t);
        for (auto& temp : adj[t]) {
            deg[temp]--;
            if (deg[temp] == 0) {
                q.push(temp);
            }
        }
    }

    string s(vec.begin(), vec.end());
    return s;
}

int main() {
    string dict[] = {"baa", "abcd", "abca", "cab", "cad"};
    int N = 5;
    int K = 4;

    string order = findOrder(dict, N, K);
    cout << "Order of characters in alien language: " << order << endl;

    return 0;
}
