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
        const double POUND_IN_GRAMS = 453.59237;

        public double PricePerPound()
        {
            double priceInPounds = (pricePerIndicatedGram * POUND_IN_GRAMS) / indicatedGrams;
            return priceInPounds;
        }

        public void DisplayResults()
        {
            Console.WriteLine(brandOfMeat + ", which sells for $" + Math.Round(PricePerPound(), 2) + " per 1 pound");
        }
    }
}
