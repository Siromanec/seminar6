#include <iostream>
#include <vector>
#include <algorithm>
#define HASH_TABLE_SIZE 997
using std::vector;

int hashCode(int x){
    /*[1,0] and [1,997]
     * 1 mod 997 == 998 mod 997
     *
     * */
    return ((x+HASH_TABLE_SIZE)%HASH_TABLE_SIZE);
}
void hashTable(vector<vector<int>>& points, int *table){
    for (vector<int> it : points)
    {
        ++table[hashCode(it[0] + it[1])];
    }
    //return table;
}
int main(){
    vector<vector<int>> points {{0,0},{2,0},{1,1}, {2,2}};//{-1,0},{0,0},{1,0}, {2,0}}
    static int table[HASH_TABLE_SIZE];
    hashTable(points, table);
    int si, sk, count = 0;
    for (vector<int> iti : points)
    {
        si = iti[0] + iti[1]; // x2 + y2
        for (vector<int> itk : points){
            sk = itk[0] + itk[1]; // x3 + y3
            if (iti!=itk){
                count += table[hashCode(2*si-sk)]; //x1 + y1 == 2*(x2 + y2) - (x3+y3)
            }
        }

    }
    for (int & i : table) {
        std::cout<<i;
    }
    std::cout<<std::endl;
    for (int & i : table) {
        i = 0;
    }
    for (int & i : table) {
        std::cout<<i;
    }
    std::cout<<std::endl;
    std::cout<<count;
    //delete[] table;
    return 0;
}