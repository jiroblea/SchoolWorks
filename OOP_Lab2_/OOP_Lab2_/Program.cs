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
        public static double GetNumOfCases()
        {
            Console.WriteLine("This program calculates the gross profit of your sales project,\nafter deducting your expenses and payment to the Student Government Association from it.\n");
            Console.WriteLine("Enter the number of cases sold: ");
            string input = Console.ReadLine();
            double numOfCases = Convert.ToDouble(input);
            return numOfCases;
        }

        public static double GetSalePrice()
        {
            Console.WriteLine("Enter the sale price per granola bar: ");
            string input = Console.ReadLine();
            double salePrice = Convert.ToDouble(input);
            return salePrice;
        }


        // OOP-Lab2-Num9
        public static string GetNameEmployee()
        {
            Console.WriteLine("Enter your LAST NAME, FIRST NAME and MIDDLE INITIAL: ");
            string nameEmployee = Console.ReadLine();
            return nameEmployee;
        }

        public static double GetSalesAmnt()
        {
            Console.WriteLine("Enter your Sales Amount: ");
            string input = Console.ReadLine();
            double salesAmnt = Convert.ToDouble(input);
            return salesAmnt;
        }


        // OOP-Lab2-Num10
        public static string GetAddress()
        {
            Console.WriteLine("Enter property address: ");
            string address = Console.ReadLine();
            return address;
        }

        public static double GetPriorYearValue()
        {
            Console.WriteLine("Enter prior year's value: ");
            string input = Console.ReadLine();
            double priorYearValue = Convert.ToDouble(input);
            return priorYearValue;
        }


        static void Main(string[] args)
        {
            DateTime timeStamp = DateTime.Now;

            
            // OOP-Lab2-Num5
            ConvertFahrenheit fahrenheit1 = new ConvertFahrenheit();

            fahrenheit1.temperature = GetTemperature();
            fahrenheit1.DisplayResults();

            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));

            Console.ReadLine();
            // OOP-Lab2-Num6
            ConvertMeters meter1 = new ConvertMeters();

            meter1.meters = GetMeters();
            meter1.DisplayResult();

            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));

            Console.ReadLine();
            // OOP-Lab2-Num7
            CalculateTip tip1 = new CalculateTip();

            tip1.bill = GetBill();
            tip1.currencyType = GetCurrency();
            tip1.DisplayConfirmation();
            tip1.DisplayResults();

            Console.WriteLine("Time Stamp\t\t\t: " + timeStamp.ToString("F"));
            
            Console.ReadLine();
            // OOP-Lab2-Num8
            CalculateProfit profit1 = new CalculateProfit();

            profit1.numOfCases = GetNumOfCases();
            profit1.salePrice = GetSalePrice();
            profit1.DisplayResults();

            Console.WriteLine("Time Stamp\t\t\t\t\t: " + timeStamp.ToString("F"));

            Console.ReadLine();
            // OOP-Lab2-Num9
            TakeHomePay employee1 = new TakeHomePay();

            employee1.DisplayInfo();
            employee1.nameEmployee = GetNameEmployee();
            employee1.salesAmnt = GetSalesAmnt();
            employee1.DisplayResults();

            Console.WriteLine("Time Stamp\t\t: " + timeStamp.ToString("F"));

            Console.ReadLine();
            // OOP-Lab2-Num10
            CalculateProposedTax propertyTax1 = new CalculateProposedTax();

            propertyTax1.address = GetAddress();
            propertyTax1.priorYearValue = GetPriorYearValue();
            propertyTax1.DisplayResults();

            Console.WriteLine("Time Stamp\t\t\t: " + timeStamp.ToString("F"));
        }
    }
}
