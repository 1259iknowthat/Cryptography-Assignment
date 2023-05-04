#include <iostream>
#include <sstream>
using namespace std;

class ROT{
    private:
        string s;
        const int shift = 13;
    
    public:
        ROT(){};
        ROT(string s){
            this->s = s;
        }

        friend istream& operator>>(istream& in, ROT& input){
            cout << "Please input your string: ";
            getline(in, input.s);
            return in;
        }

        void encode(){
            string result = "";
            for (size_t i = 0; i < this->s.length(); i++) {
                if (isupper(this->s[i]))
                    result += (this->s[i] + this->shift - 'A') % 26 + 'A';
                else if (islower(this->s[i]))
                    result += (this->s[i] + this->shift - 'a') % 26 + 'a';
                else    
                    result += this->s[i];
            }
            this->s = result;
        }

        void decode(){
            string result = "";
            for (size_t i = 0; i < this->s.length(); i++) {
                if (isupper(this->s[i]))
                    result += (this->s[i] - this->shift - 'A' + 26) % 26 + 'A';
                else if (islower(this->s[i]))
                    result += (this->s[i] - this->shift - 'a' + 26) % 26 + 'a';
                else    
                    result += this->s[i];
            }
            this->s = result;
        }

        friend ostream& operator<<(ostream& out, ROT& output){
            out << "Here is your output: ";
            out << output.s;
            return out;
        }

};


int main(){
    ROT text;
    cin >> text;
    text.encode();
    cout << text << endl;
    text.decode();
    cout << text << endl;
}