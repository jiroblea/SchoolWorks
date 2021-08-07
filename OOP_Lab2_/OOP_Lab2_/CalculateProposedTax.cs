using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab2_
{
    class CalculateProposedTax
    {
        public string address;
        public double priorYearValue;

        // contants
        const double INCREASED_ASSESSED_VALUE = 0.027;
        const double TAX_EXEMPTION = 25000;
        const double CURRENT_MILEAGE_RATE = 0.01003; // $10.03 PER $1000

        private double NewAssessedValue()
        {
            double newAssessedValue = priorYearValue + (priorYearValue * INCREASED_ASSESSED_VALUE);
            return newAssessedValue;
        }

        private double CurrentProposedTax()
        {
            double assessedValuePriorTax = NewAssessedValue() - TAX_EXEMPTION;
            double proposedTax = assessedValuePriorTax * CURRENT_MILEAGE_RATE;
            return proposedTax;
        }

        public void DisplayResults()
        {
            Console.WriteLine("Property address\t\t: " + address);
            Console.WriteLine("Prior year's assessed value\t: $" + priorYearValue);
            Console.WriteLine("New assessed value\t\t: $" + Math.Round(NewAssessedValue(), 2));
            Console.WriteLine("Proposed tax for current year\t: $" + Math.Round(CurrentProposedTax(), 2));
        }
    }
}
