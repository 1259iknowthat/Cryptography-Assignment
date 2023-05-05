#include <iostream>
#include <sstream>
using namespace std;

string decode(string s, int8_t shift){
    string result = "";
        for (size_t i = 0; i < s.length(); i++) {
            if (isupper(s[i]))
                result += (s[i] + shift - 'A') % 26 + 'A';
            else if (islower(s[i]))
                result += (s[i] + shift - 'a') % 26 + 'a';
            else    
                result += s[i];
        }
    return result;
}

void bruteforce(string s){
    printf("Brute-force's output:\n");
    for (int8_t i = 1; i < 26; i++){
        string tmp = decode(s, i);
        printf("Decoded string: %s\n", tmp.c_str());
        printf("Shift: %d\n", i);    
    }
}

int main(){
    string input;
    cout << "Please provide the encoded string: ";
    getline(cin, input);
    bruteforce(input);
}
