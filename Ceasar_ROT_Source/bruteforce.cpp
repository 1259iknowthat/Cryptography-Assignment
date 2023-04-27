#include <iostream>

using namespace std;

string decode(string s, int shift){
    string result = "";
        for (int i = 0; i < s.length(); i++) {
            if (isupper(s[i]))
                result += char(int(s[i] + shift - 65) % 26 + 65);
            else if (islower(s[i]))
                result += char(int(s[i] + shift - 97) % 26 + 97);
            else    
                result += s[i];
        }
    return result;
}

void bruteforce(string s){
    printf("Brute-force's output:\n");
    for (int i = 0; i < 26; i++){
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