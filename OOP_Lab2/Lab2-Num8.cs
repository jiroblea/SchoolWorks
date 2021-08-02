// written by jeron
using System;

public class Main4Class
{

    public static void Main(String[] args)
    {
        double numOfCases;
        double salePrice, earnings, expenses, profit, studentGovFee, newProfit;

            numOfCases = GetNumOfCases("Cases");
            salePrice = GetSalePrice("SalePrice");
            earnings = GetEarnings(salePrice, numOfCases);
            expenses = GetExpenses(numOfCases);
            profit = GetProfit(earnings, expenses);
            studentGovFee = GetFee(profit);
            newProfit = GetNewProfit(profit, studentGovFee);
            DisplayResults(profit, studentGovFee, newProfit);
        
    }

    private static double GetNumOfCases(string label)
    {
        string input;
        double numOfCases;

        Console.WriteLine("This program calculates the gross profit of your sales project,\nafter deducting your expenses and payment to the Student Government Association from it.");
        Console.WriteLine(" ");
        Console.WriteLine("Enter the number of cases sold: ");
        input = Console.ReadLine();
        numOfCases = Convert.ToDouble(input);

        return numOfCases;
    }

    private static double GetSalePrice(string label)
    {
        string input2;
        double salePrice;

        Console.WriteLine("Enter the sale price per granola bar: ");
        input2 = Console.ReadLine();
        salePrice = Convert.ToDouble(input2);

        return salePrice;
    }

    private static double GetEarnings(double numOfCases, double salePrice)
    {
        double pricePerCase,earnings;

        pricePerCase = salePrice * 12;
        earnings = pricePerCase * numOfCases;

        return earnings;
    }

    private static double GetExpenses(double numOfCases)
    {
        double expenses;

        expenses = numOfCases * 5.00;

        return expenses;
    }

    private static double GetProfit(double earnings, double expenses)
    {
        if (earnings < expenses)
        {
            Console.WriteLine("You have no profit from this project!\nPress any key to exit");
            Console.Read();
            return 0;
        }

        else
        {
            double profit;
            profit = earnings - expenses;
            return profit;
        }
        
    }

    private static double GetFee(double profit)
    {
        double studentGovFee;

        studentGovFee = profit * 10 / 100;

        return studentGovFee;
    }

    private static double GetNewProfit(double profit, double studentGovFee)
    {
        double newProfit;

        newProfit = profit - studentGovFee;

        return newProfit;
    }

    public static void DisplayResults(double profit, double studentGovFee, double newProfit)
    {
        Console.WriteLine("Your original profit is {0:c}.", profit);
        Console.WriteLine(" ");
        Console.WriteLine("When deducted by the {0:c}, the final profit becomes: {1:c}", studentGovFee, newProfit);
    }
}