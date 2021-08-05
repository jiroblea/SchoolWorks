using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab2_
{
    class ConvertMeters
    {
        public double meters;

        private double CalculateInches()
        {
            double inches = meters * 39.37;
            return Math.Round(inches, 2);
        }

        private double CalculateFeet()
        {
            double feet = CalculateInches() / 12;
            return Math.Floor(feet);
        }

        private double CalculateNewInches()
        {
            double newInches = CalculateInches() % 12;
            return Math.Round(newInches, 2);
        }

        public void DisplayResult()
        {
            Console.WriteLine("Original value\t: " + meters);
            Console.WriteLine("Converted value\t: " + CalculateFeet() + " feet and " + CalculateNewInches() + " inch[es]");
        }
    }
}
