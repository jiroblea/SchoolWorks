using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab2_
{
    class CalculateTip
    {
        public double bill;
        public string currencyType;

        // constants
        const double TAX_RATE = 0.09;
        const double TIP_RATE_15 = 0.15;
        const double TIP_RATE_20 = 0.20;

        public void DisplayConfirmation()
        {
            Console.WriteLine("You entered: " + bill.ToString() + " " + currencyType + "\nPress Enter to continue.");
            Console.Read();
            return;
        }

        private double CalculateTax()
        {
            double taxedAmnt = bill * TAX_RATE;
            return taxedAmnt;
        }

        private double CalculateTaxedBill()
        {
            double taxedBill = bill + CalculateTax();
            return taxedBill;
        }

        private double ComputeTip15()
        {
            double tip15 = CalculateTaxedBill() * TIP_RATE_15;
            return Math.Round(tip15, 2);
        }

        private double ComputeTip20()
        {
            double tip20 = CalculateTaxedBill() * TIP_RATE_20;
            return Math.Round(tip20, 2);
        }

        private double FinalAmnt15()
        {
            double totalAmntDue15 = CalculateTaxedBill() + ComputeTip15();
            return Math.Round(totalAmntDue15, 2);
        }

        private double FinalAmnt20()
        {
            double totalAmntDue20 = CalculateTaxedBill() + ComputeTip20();
            return Math.Round(totalAmntDue20, 2);
        }

        public void DisplayResults()
        {
            Console.WriteLine("Bill amount entered\t\t: " + bill.ToString() + " " + currencyType);
            Console.WriteLine("Amount of tax\t\t\t: " + CalculateTax() + " " + currencyType);
            Console.WriteLine("Bill with tax\t\t\t: " + CalculateTaxedBill() + " " + currencyType);
            Console.WriteLine("Amount of tip for 15% charge\t: " + ComputeTip15() + " " + currencyType);
            Console.WriteLine("Total amount due to 15%\t\t: " + FinalAmnt15() + " " + currencyType);
            Console.WriteLine("Amount of tip for 20% charge\t: " + ComputeTip20() + " " + currencyType);
            Console.WriteLine("Total amount due to 20%\t\t: " + FinalAmnt20() + " " + currencyType);
        }
    }
}
