using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab2_
{
    class TakeHomePay
    {
        public string nameEmployee;
        public double salesAmnt;

        // constants
        const double PAY_RATE = 0.07;
        const double FED_TAX_RATE = 0.18;
        const double RETIREMENT_CONTRIBUTION = 0.15;
        const double SOCIAL_SECURITY_RATE = 0.09;

        public void DisplayInfo()
        {
            Console.WriteLine("This program calculates your take home pay after factoring in your sales amount and tax deductions.\n");
            Console.WriteLine("Press any key to start.");
            Console.Read();
        }

        private double GetPaymentEmployee()
        {
            double paymentEmployee = salesAmnt * PAY_RATE;
            return paymentEmployee;
        }

        private double GetFedTax()
        {
            double federalTax = GetPaymentEmployee() * FED_TAX_RATE;
            return federalTax;
        }

        private double GetContribution()
        {
            double retirementContribution = GetPaymentEmployee() * RETIREMENT_CONTRIBUTION;
            return retirementContribution;
        }

        private double GetSocSecTax()
        {
            double socialSecurityTax = GetPaymentEmployee() * SOCIAL_SECURITY_RATE;
            return socialSecurityTax;
        }

        private double GetTakeHomePay()
        {
            double takeHomePay = GetPaymentEmployee() - GetFedTax() - GetContribution() - GetSocSecTax();
            return takeHomePay;
        }

        public void DisplayResults()
        {
            Console.WriteLine("Employee name\t\t: " + nameEmployee);
            Console.WriteLine("Sales amount\t\t: $" + salesAmnt);
            Console.WriteLine("Original payment\t: $" + Math.Round(GetPaymentEmployee(), 2));
            Console.WriteLine("\nThe following are tax deductions: " );
            Console.WriteLine("Federal tax\t\t: $" + Math.Round(GetFedTax(), 2));
            Console.WriteLine("Retirement contribution\t: $" + Math.Round(GetContribution(), 2));
            Console.WriteLine("Social security tax\t: $" + Math.Round(GetSocSecTax(), 2));
            Console.WriteLine("\nTake-home pay\t\t: $" + Math.Round(GetTakeHomePay(), 2));
        }
    }
}
