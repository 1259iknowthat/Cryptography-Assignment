#include <iostream>

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
            for (int i = 0; i < this->s.length(); i++) {
                if (isupper(this->s[i]))
                    result += char(int(this->s[i] + this->shift - 65) % 26 + 65);
                else if (islower(this->s[i]))
                    result += char(int(this->s[i] + this->shift - 97) % 26 + 97);
                else    
                    result += this->s[i];
            }
            this->s = result;
        }

        void decode(){
            string result = "";
            for (int i = 0; i < this->s.length(); i++) {
                if (isupper(this->s[i]))
                    result += char(int(this->s[i] - this->shift - 65 + 26) % 26 + 65);
                else if (islower(this->s[i]))
                    result += char(int(this->s[i] - this->shift - 97 + 26) % 26 + 97);
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