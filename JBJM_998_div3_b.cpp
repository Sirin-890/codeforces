#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric> // Required for iota


using namespace std;

int main() {
    int t, n, m;
    cin >> t;

    while (t--) {
        cin >> n >> m;
        vector<vector<int> > mat(n, vector<int>(m));

        // Input matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> mat[i][j];
            }
        }

        for (auto &row : mat) {
            sort(row.begin(), row.end());
        }

        vector<int> index(n);
        iota(index.begin(), index.end(), 0); 
        struct Compare {
    vector<vector<int> > &mat;
    Compare(vector<vector<int> > &m) : mat(m) {}
    bool operator()(int a, int b) {
        return mat[a][0] < mat[b][0];
    }
};

Compare cmp(mat);
sort(index.begin(), index.end(), cmp);

for(int i=0;i<n;i++){
    cout <<index[i];
}
cout <<"------------------------------------------------------------";
        
        bool valid = true;
        for (int j = 0; j < m; j++) {
            for (int i = 1; i < n; i++) {
                if (mat[index[i]][j] < mat[index[i - 1]][j]) {
                    valid = false;
                    break;
                }
            }
            if (!valid) break;
        }

        for (int j = 0; j < m - 1; j++) {
            if (mat[index[n - 1]][j] >= mat[index[0]][j + 1]) {
                valid = false;
                break;
            }
        }

        // Output result
        if (valid) {
            for (int i = 0; i < n; i++) {
                cout << index[i] + 1 << " "; // Convert to 1-based index
            }
            cout << endl;
        } else {
            cout << -1 << endl;
        }
    }

    return 0;
}
