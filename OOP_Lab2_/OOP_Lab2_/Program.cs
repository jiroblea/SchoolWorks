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


        // OOP-Lab2-Num6
        public static double GetMeters()
        {
            Console.WriteLine("Enter meters: ");
            string input = Console.ReadLine();
            double meters = Convert.ToDouble(input);
            return meters;
        }


        // OOP-Lab2-Num7
        public static double GetBill()
        {
            Console.WriteLine("This calculates the total amount after applying tax and tip to the bill.\n");
            Console.WriteLine("Enter the current bill: ");
            string input = Console.ReadLine();
            double bill = Convert.ToDouble(input);
            return bill;
        }

        public static string GetCurrency()
        {
            Console.WriteLine("Enter currency type (optional): ");
            string currencyType = Console.ReadLine();
            return currencyType;
        }


        // OOP-Lab2-Num8



        static void Main(string[] args)
        {
            DateTime timeStamp = DateTime.Now;

            
            // OOP-Lab2-Num5
            ConvertFahrenheit fahrenheit1 = new ConvertFahrenheit();

            fahrenheit1.temperature = GetTemperature();
            fahrenheit1.DisplayResults();

            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));


            // OOP-Lab2-Num6
            ConvertMeters meter1 = new ConvertMeters();

            meter1.meters = GetMeters();
            meter1.DisplayResult();

            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));


            // OOP-Lab2-Num7
            CalculateTip tip1 = new CalculateTip();

            tip1.bill = GetBill();
            tip1.currencyType = GetCurrency();
            tip1.DisplayConfirmation();
            tip1.DisplayResults();

            Console.WriteLine("Time Stamp\t\t\t: " + timeStamp.ToString("F"));

            
            // OOP-Lab2-Num8

        }
    }
}
