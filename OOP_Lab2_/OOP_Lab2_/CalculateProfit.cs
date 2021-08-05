using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab2_
{
    class CalculateProfit
    {
        public double numOfCases;
        public double salePrice;

        // constants
        const int BARS_EACH_CASE = 12;
        const double PRICE_EACH_CASE = 5;
        const double STUDENT_GOV_FEE = 0.10;

        private double GetEarnings()
        {
            double pricePerCase = salePrice * BARS_EACH_CASE;
            double earnings = pricePerCase * numOfCases;
            return earnings;
        }

        private double GetExpenses()
        {
            double expenses = numOfCases * PRICE_EACH_CASE;
            return expenses;
        }

        private double GetProfit()
        {
            if (GetEarnings() < GetExpenses())
            {
                Console.WriteLine("You have no profit from this project!\nPress any key to exit");
                Console.Read();
                return 0;
            }
            else
            {
                double profit = GetEarnings() - GetExpenses();
                return profit;
            }
        }

        private double GetFee()
        {
            double studentGovFee = GetProfit() * STUDENT_GOV_FEE;
            return studentGovFee;
        }

        private double GetNewProfit()
        {
            double newProfit = GetProfit() - GetFee();
            return newProfit;
        }

        public void DisplayResults()
        {
            Console.WriteLine("\nOriginal profit\t\t\t\t\t: $" + Math.Round(GetProfit(), 2));
            Console.WriteLine("Deducted for Student Government Association\t: $" + Math.Round(GetFee(), 2));
            Console.WriteLine("Final Profit\t\t\t\t\t: $" + Math.Round(GetNewProfit(), 2));
        }
    }
}
