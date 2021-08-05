using System;

namespace OOP_Lab2_
{
    class Program
    {
        // OOP-Lab2-Num5
        public static double GetTemperature()
        {
            Console.WriteLine("Enter temperature in Fahrenheit:");
            string input = Console.ReadLine();
            double temperature = Convert.ToDouble(input);
            return temperature;
        }

        static void Main(string[] args)
        {
            DateTime timeStamp = DateTime.Now;

            // OOP-Lab2-Num5
            ConvertFahrenheit fahrenheit1 = new ConvertFahrenheit();

            fahrenheit1.temperature = GetTemperature();
            fahrenheit1.DisplayResults();

            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));
        }
    }
}
