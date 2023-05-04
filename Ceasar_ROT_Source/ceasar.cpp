#include <iostream>
#include <sstream>
using namespace std;

class Ceasar{
    private:
        string s;
        int shift;

    public:
        Ceasar(){};
        Ceasar(string s, int shift){
            this->s = s;
            this->shift = shift;
        };

        friend istream& operator>>(istream& in, Ceasar& input){
            cout << "Please input your string: ";
            getline(in, input.s);
            cout << "Please input your shift: ";
            cin >> input.shift;
            return in;
        }

        void encode(){
            string result = "";
            for (size_t i = 0; i < this->s.length(); ++i) {
                if (isupper(this->s[i]))
                    result += (this->s[i] + this->shift - 'A' + 26) % 26 + 'A';
                else if (islower(this->s[i]))
                    result += (this->s[i] + this->shift - 'a' + 26) % 26 + 'a';
                else    
                    result += this->s[i];
            }
            this->s = result;
        }

        friend ostream& operator<<(ostream& out, Ceasar& output){
            out << "Here is your encoded string: ";
            out << output.s;
            return out;
        }
};

int main(){
    Ceasar text;
    cin >> text;
    text.encode();
    cout << text << endl;
}