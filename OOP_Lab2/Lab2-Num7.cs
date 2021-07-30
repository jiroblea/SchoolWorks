using System;

public class Main3Class
{
    public static void Main(String[] args)
    {
        double bill, taxAmnt, taxedBill, tip15, tip20, totalAmntDue15, totalAmntDue20;
        string currencyType;

            bill = GetBill("Bill");
            currencyType = GetCurrency("Currency");
            DisplayConfirmation(bill, currencyType);
            taxAmnt = CalculateTax(bill);
            taxedBill = CalculateTaxedBill(bill, taxAmnt);
            tip15 = ComputeTip15(taxedBill);
            tip20 = ComputeTip20(taxedBill);
            totalAmntDue15 = FinalAmnt15(taxedBill,tip15);
            totalAmntDue20 = FinalAmnt20(taxedBill,tip20);
            DisplayResults(bill, currencyType, taxAmnt, taxedBill, tip15, tip20, totalAmntDue15, totalAmntDue20);
    }

    private static double GetBill(string label)
    {
        string input;
        double bill;

        Console.WriteLine("This program calculates the total amount due after applying tax and tip to your bill.");
        Console.WriteLine("Please enter the current bill: ");
        input = Console.ReadLine();
        bill = Convert.ToDouble(input);

        return bill;
    }

    private static string GetCurrency(string label)
    {
        string currencyType;

        Console.WriteLine("Enter your currency type (this is optional, press the Enter key to skip): ");
        currencyType = Console.ReadLine();

        return currencyType;

    }

    public static void DisplayConfirmation(double bill, string currencyType)
    {
        Console.WriteLine("You entered " + bill.ToString() + currencyType + ". Press Enter to continue.");
        Console.Read();

    }

    private static double CalculateTax(double bill)
    {
        double taxAmnt;

        taxAmnt = bill * 9 / 100;

        return taxAmnt;
    }

    private static double CalculateTaxedBill (double bill, double taxAmnt)
    {
        double taxedBill;

        taxedBill = bill + taxAmnt;

        return taxedBill;
    }

    private static double ComputeTip15(double taxedBill)
    {
        double tip15;

        tip15 = taxedBill * 15 / 100;

        return tip15;
    }

    private static double FinalAmnt15(double taxedBill, double tip15)
    {
        double totalAmntDue15;

        totalAmntDue15 = taxedBill + tip15;

        return totalAmntDue15;
    }

    private static double ComputeTip20(double taxedBill)
    {
        double tip20;

        tip20 = taxedBill * 20 / 100;

        return tip20;
    }

    private static double FinalAmnt20(double taxedBill, double tip20)
    {
        double totalAmntDue20;

        totalAmntDue20 = taxedBill + tip20;

        return totalAmntDue20;
    }

    public static void DisplayResults(double bill, string currencyType, double taxAmnt, double taxedBill, double tip15, double tip20, double FinalAmnt15, double FinalAmnt20)
    {
        Console.WriteLine("The bill amount you entered is : " + bill.ToString() + " " + currencyType);
        Console.WriteLine(" ");
        Console.WriteLine("The amount of tax is " + taxAmnt.ToString() + " " + currencyType + ", and the bill with tax is: " + taxedBill.ToString() + " " + currencyType +  ".");
        Console.WriteLine(" ");
        Console.WriteLine("The amount of tip for the 15% charge is " + tip15.ToString() + " " + currencyType + ", and the total amount due for a 15% charge on tip is: " + FinalAmnt15.ToString() + " " + currencyType + ".");
        Console.WriteLine(" ");
        Console.WriteLine("The amount of tip for the 20% charge is " + tip20.ToString() + " " + currencyType + ", and the total amount due for a 20% charge on tip is: " + FinalAmnt20.ToString() + " " + currencyType + ".");

    }
}