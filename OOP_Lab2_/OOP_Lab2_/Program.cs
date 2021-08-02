using System;

namespace OOP_Lab2_
{
    class Program
    {
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

            ConvertFahrenheit fahrenheit1 = new ConvertFahrenheit();

            fahrenheit1.temperature = GetTemperature();
            fahrenheit1.DisplayResults();

            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));
        }
    }
}
