using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab1
{
    class ComputeMoneyToReceive
    {
        // amounts
        public int amountOfCasesSold;
        public int amountOfBarsInEachCase;
        public double percentRequiredToGive;

        // prices in dollars
        const double PRICE_OF_EACH_CASE = 100; // an expense
        const double PRICE_OF_EACH_BAR = 1.50; // an earning

        // compute the total earnings
        public double TotalEarnings()
        {
            int amountOfBarsSold = amountOfCasesSold * amountOfBarsInEachCase;
            double totalEarnings = amountOfBarsSold * PRICE_OF_EACH_BAR;
            return totalEarnings;
        }

        // compute the amount given to the Student Organization
        public double ExpenseGiven()
        {
            double expenseGiven = TotalEarnings() * percentRequiredToGive;
            return expenseGiven;
        }

        // compute the total expenses
        public double TotalExpenses()
        {
            double expenseForEachCase = amountOfCasesSold * PRICE_OF_EACH_CASE;
            double totalExpenses = expenseForEachCase + ExpenseGiven();
            return totalExpenses;
        }

        // compute the total amount of money received by the computer club
        public double TotalAmountReceive()
        {
            double totalAmountReceive = TotalEarnings() - TotalExpenses();
            return totalAmountReceive;
        }

        public void DisplayResults()
        {
            Console.WriteLine("Amount Receive\t\t\t: $" + TotalAmountReceive());
            Console.WriteLine("Given to Student Organization\t: $" + ExpenseGiven());
        }
    }
}
