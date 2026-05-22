class Solution {
public:

    string encode(vector<string>& strs) {
        std::string crypt = "";
        for (std::string& s : strs) {
            crypt += std::to_string(s.length());
            crypt += "!";
            crypt += s;
        }
        return crypt;
    }

    vector<string> decode(string s) {
        std::vector<std::string> strs;
        std::string num = "";
        int numI = -1;
        for (int i = 0; i < s.length(); i++) {
            if (s.at(i) != '!') {
                num += s.at(i);
            }
            else {
                numI = std::stoi(num);
                strs.push_back(s.substr(i+1, numI));
                i += numI;
                num = "";
            }
        }
        return strs;
    }
};
