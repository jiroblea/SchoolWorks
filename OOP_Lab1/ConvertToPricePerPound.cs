using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab1
{
    class ConvertToPricePerPound
    {
        // variables
        public string brandOfMeat;
        public double pricePerIndicatedGram; // in dollars
        public double indicatedGrams;

        // conversion: 1 lb = 453.59237 g
        const double POUNDINGRAMS = 453.59237;

        public double PricePerPound()
        {
            double priceInPounds = (pricePerIndicatedGram * POUNDINGRAMS) / indicatedGrams;
            return priceInPounds;
        }

        public void DisplayResults()
        {
            Console.WriteLine(brandOfMeat + ", which sells for $" + Math.Round(PricePerPound(), 2) + " per 1 pound");
        }
    }
}
