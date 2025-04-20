#include <string>
#include <vector>

using namespace std;

vector<int> solution(string myString) {
    vector<int> answer;
    int c = 0;
    for (int i = 0 ; i < myString.size(); i++){
        if (myString[i] == 'x'){
            answer.push_back(c);
            c = 0;
        }else {
            c++;
        }
    }
    answer.push_back(c);
    return answer;
}