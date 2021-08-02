// written by jeron 
using System;

public class Main5Class
{
    public static void Main(String[] args)
    {
        string nameEmployee;
        double salesAmnt, paymentEmployee, federalTax, retirementContribution, socialSecurityTax, takeHomePay;

            DisplayInfo("Information");
            nameEmployee = GetNameEmployee("Name");
            salesAmnt = GetSalesAmnt("Sales");
            paymentEmployee = GetPaymentEmployee(salesAmnt);
            federalTax = GetFedTax(paymentEmployee);
            retirementContribution = GetContribution(paymentEmployee);
            socialSecurityTax = GetSocSecTax(paymentEmployee);
            takeHomePay = GetTakeHomePay(paymentEmployee, federalTax, retirementContribution, socialSecurityTax);

            DisplayResults(nameEmployee, salesAmnt, paymentEmployee, federalTax, retirementContribution, socialSecurityTax, takeHomePay);

            return;
    }

    public static void DisplayInfo(string label)
    {
        Console.WriteLine("This program calculates your take home pay after factoring in your sales amount and tax deductions.");
        Console.WriteLine(" ");
        Console.WriteLine("Press any key to start.\n");
        Console.Read();
    }

    private static string GetNameEmployee(string label)
    {
        string nameEmployee;

        Console.WriteLine("Enter your LAST NAME, FIRST NAME and MIDDLE INITIAL: ");
        nameEmployee = Console.ReadLine();

        return nameEmployee;
    }

    private static double GetSalesAmnt(string label)
    {
        string input;
        double salesAmnt;
        
        Console.WriteLine("Enter your Sales Amount: ");
        input = Console.ReadLine();
        salesAmnt = Convert.ToDouble(input);

        return salesAmnt;
    }

    private static double GetPaymentEmployee(double salesAmnt)
    {
        double paymentEmployee;

        paymentEmployee = salesAmnt * 7 / 100;

        return paymentEmployee;
    }

    private static double GetFedTax(double paymentEmployee)
    {
        double federalTax;

        federalTax = paymentEmployee * 18 / 100;

        return federalTax;
    }

    private static double GetContribution(double paymentEmployee)
    {
        double retirementContribution;

        retirementContribution = paymentEmployee * 15 / 100;

        return retirementContribution;
    }

    private static double GetSocSecTax(double paymentEmployee)
    {
        double socialSecurityTax;

        socialSecurityTax = paymentEmployee * 9 / 100;

        return socialSecurityTax;
    }

    private static double GetTakeHomePay(double paymentEmployee, double federalTax, double retirementContribution, double socialSecurityTax)
    {
        double takeHomePay;

        takeHomePay = paymentEmployee - federalTax - retirementContribution - socialSecurityTax;

        return takeHomePay;
    }

    public static void DisplayResults(string nameEmployee, double salesAmnt, double paymentEmployee, double federalTax, double retirementContribution, double socialSecurityTax, double takeHomePay)
    {
        Console.WriteLine("Name: " + nameEmployee);
        Console.WriteLine("Sales Amount: {0:c} .\n", salesAmnt);
        Console.WriteLine("Original Payment: {0:c} .\n", paymentEmployee);
        Console.WriteLine("\tTax Deductions\n");
        Console.WriteLine("Federal Tax: {0:c} .", federalTax);
        Console.WriteLine("Retirement Contribution: {0:c} .", retirementContribution);
        Console.WriteLine("Social Security Tax: {0:c} .\n\n", socialSecurityTax);
        Console.WriteLine("Take-home Pay : {0:c} .", takeHomePay);
    }
}