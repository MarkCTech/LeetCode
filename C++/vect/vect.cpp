
// C++ program to print the elements
// of the vectors
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int count_numbers( const vector<int> &vec) {
    int count {0};
    size_t index {0};
    
    while (index < vec.size() && vec.at(index) != -99  ) {
        ++count;
        ++index;
    }
    return count;
}



int main() {
    const vector<int> int_vec {10,20,30,-30,-40,-7,-99};
    //count_numbers(int_vec);

    for_each(int_vec.begin(),
        int_vec.end(),
        [](const auto& elem) {
            cout << elem << " ";
        });
    return 0;
}