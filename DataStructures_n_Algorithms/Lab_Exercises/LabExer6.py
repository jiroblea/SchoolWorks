# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# Laboratory Exercise No. 6

# Complete the following code and then generate an equivalent code in python. 

# The completed code in C++:
"""
#include <iostream>

using namespace std;

// Certificate of Deposit Account Structure
struct CDAccount{
    double balance;
    double interestRate;
    int term;
};

CDAccount doubleInterest(CDAccount& oldAccount);

void accountBalance(CDAccount& _account);

int main() {
    CDAccount account;
    
    cout << "Enter account balance: PHP ";
    cin >> account.balance;
    cout << "Enter account interest: ";
    cin >> account.interestRate;
    cout << "Enter the number of months until maturity: ";
    cin >> account.term;
    
    accountBalance(account);
    
    cout << "\nOld Account \n"
            << "When your CD matures in \n"
            << account.term << " months, \n"
            << "it will have a balance of PHP"
            << account.balance << endl;
            
    CDAccount accountNew;
    accountNew = doubleInterest(account);
    
    accountBalance(accountNew);
    
    cout << "\nNew Account \n"
            << "When your CD matures in \n"
            << account.term << " months, \n"
            << "it will have a balance of PHP"
            << accountNew.balance << endl;
    
    system("pause>0");
    return 0;
}

void accountBalance(CDAccount& _account){
    double rateFraction, interest;
    rateFraction = _account.interestRate / 100.0;
    interest = _account.balance * (rateFraction * (_account.term / 12.0));
    _account.balance = _account.balance + interest;
}

CDAccount doubleInterest(CDAccount& oldAccount){
    CDAccount temp;
    temp = oldAccount;
    temp.interestRate = 2 * oldAccount.interestRate;
    return temp;
}
"""


# an equivalent code in Python:

class CDAccount:
    def __init__(self, balance: float, interest_rate: float, term: int):
        self.balance = balance
        self.interest_rate = interest_rate
        self.term = term
    

    def accountBalance(self):
        rate_fraction = self.interest_rate / 100.0
        interest = self.balance * (rate_fraction * (self.term / 12.0))
        self.balance = self.balance + interest
        return None


    def doubleInterest(self):
        temp = CDAccount
        temp = self
        temp.interest_rate = 2 * self.interest_rate
        return temp


def main():
    account = CDAccount
    
    account.balance = float(input("Enter account balance: Php "))
    account.interest_rate = float(input("Enter account interest: "))
    account.term = int(input("Enter the number of months until maturity: "))

    account.accountBalance(account)

    print("\nOld Account")
    print(f"When your account matures in {account.term} months,")
    print(f"it will have a balance of Php{account.balance}")

    accountNew = CDAccount
    accountNew.doubleInterest(account)
    
    accountNew.accountBalance(accountNew)

    print("\nNew Account")
    print(f"When your account matures in {account.term} months,")
    print(f"it will have a balance of Php{accountNew.balance}")


if __name__ == "__main__":
    main()
