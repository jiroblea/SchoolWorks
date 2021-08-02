using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab2_
{
    class ConvertFahrenheit
    {
        public double temperature;

        private double CalculateCelsius()
        {
            double celsius = (temperature - 32) * 5 / 9;
            return Math.Round(celsius, 2);
        }

        public void DisplayResults()
        {
            Console.WriteLine("Original Value\t: " + temperature + " Fahrenheit");
            Console.WriteLine("Converted Value\t: " + CalculateCelsius() + " Celsius");
        }
    }
}
