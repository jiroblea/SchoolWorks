using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab1
{
    class CommissionedSalesEmployee
    {
        public string employeeName;
        public double totalSales;
        public double earningPercentage;
        public double taxRatePercentage;
        public double retirementPercentage;
        public double socialSecurityPercentage;

        public double GrossPay()
        {
            return Math.Round(totalSales * earningPercentage, 3);
        }

        public double TaxWithheld()
        {
            return Math.Round(GrossPay() * taxRatePercentage, 3);
        }

        public double RetirementContribution()
        {
            return Math.Round(GrossPay() * retirementPercentage, 3);
        }

        public double SocialSecurityContribution()
        {
            return Math.Round(GrossPay() * socialSecurityPercentage, 3);
        }

        public double NetPay()
        {
            return Math.Round(GrossPay() - (TaxWithheld() + RetirementContribution() + SocialSecurityContribution()), 3);
        }

        public void DisplayResults()
        {
            Console.WriteLine("Employee Name\t\t\t: " + employeeName);
            Console.WriteLine("Total Sales\t\t\t: $" + totalSales);
            Console.WriteLine("Earning\t\t\t\t: $" + GrossPay());
            Console.WriteLine("Federal Tax Rate\t\t: $" + TaxWithheld());
            Console.WriteLine("Retirement Contribution\t\t: $" + RetirementContribution());
            Console.WriteLine("Social Security Contribution\t: $" + SocialSecurityContribution());
            Console.WriteLine("Take-home Pay\t\t\t: $" + NetPay());
        }
    }
}
