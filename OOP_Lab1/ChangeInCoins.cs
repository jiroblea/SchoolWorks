using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab1
{
    class ChangeInCoins
    {
        // variables
        public double change;

        // constants
        const double QUARTER = 0.25;
        const double DIME = 0.10;
        const double NICKEL = 0.05;
        const double PENNY = 0.01;

        public int NumberOfQuarter()
        {
            int numberOfQuarter = Convert.ToInt32(Math.Floor(change / QUARTER));
            return numberOfQuarter;
        }

        public int NumberOfDime()
        {
            double remains = Math.Round(change - (NumberOfQuarter() * QUARTER), 2);
            int numberOfDime = Convert.ToInt32(Math.Floor(remains / DIME));
            return numberOfDime;
        }

        public int NumberOfNickel()
        {
            double remains = Math.Round(change - ((NumberOfQuarter() * QUARTER) + (NumberOfDime() * DIME)), 2);
            int numberOfNickel = Convert.ToInt32(Math.Floor(remains / NICKEL));
            return numberOfNickel;
        }

        public int NumberOfPenny()
        {
            double remains = Math.Round(change - ((NumberOfQuarter() * QUARTER) + (NumberOfDime() * DIME) + (NumberOfNickel() * NICKEL)), 2);
            int numberOfPenny = Convert.ToInt32(Math.Floor(remains / PENNY));
            return numberOfPenny;
        }

        public void DisplayResults()
        {
            Console.WriteLine("Change\t\t\t: $" + change);
            Console.WriteLine("Number of Quarters\t: " + NumberOfQuarter());
            Console.WriteLine("Number of Dimes\t\t: " + NumberOfDime());
            Console.WriteLine("Number of Nickels\t: " + NumberOfNickel());
            Console.WriteLine("Number of Pennies\t: " + NumberOfPenny());
        }
    }
}
