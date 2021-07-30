using System;

namespace OOP_Lab1
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime timeStamp = DateTime.Now;

            // OOP Lab 1 Problem 5
            CommissionedSalesEmployee employee1 = new CommissionedSalesEmployee(); // create the object 'employee1'

            // provide the values for the attributes
            employee1.employeeName = "Nesbith Lang";
            employee1.totalSales = 161432;
            employee1.earningPercentage = 0.07;
            employee1.taxRatePercentage = 0.18;
            employee1.retirementPercentage = 0.10;
            employee1.socialSecurityPercentage = 0.06;

            // outputs
            Console.WriteLine("OOP | Laboratory 1 | Chapter 2 | Exercise 5");
            employee1.DisplayResults();
            Console.WriteLine("Time Stamp\t\t\t: " + timeStamp.ToString("F"));

            // new employee, changed the values
            CommissionedSalesEmployee employee2 = new CommissionedSalesEmployee();

            employee2.employeeName = "Will Smith";
            employee2.totalSales = 153624;
            employee2.earningPercentage = 0.10;
            employee2.taxRatePercentage = 0.19;
            employee2.retirementPercentage = 0.15;
            employee2.socialSecurityPercentage = 0.03;

            Console.WriteLine("");
            employee2.DisplayResults();
            Console.WriteLine("Time Stamp\t\t\t: " + timeStamp.ToString("F"));


            // OOP Lab 1 Problem 6
            ComputeAverageScore average1 = new ComputeAverageScore();

            average1.score1 = 25;
            average1.score2 = 5;
            average1.score3 = 10;
            average1.score4 = 21;
            average1.score5 = 45;

            Console.ReadLine();
            Console.WriteLine("\nOOP | Laboratory 1 | Chapter 2 | Exercise 6");
            average1.DisplayResults();
            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));

            // new values
            ComputeAverageScore average2 = new ComputeAverageScore();

            average2.score1 = 35;
            average2.score2 = 9;
            average2.score3 = 27;
            average2.score4 = 16;
            average2.score5 = 4;

            Console.WriteLine("");
            average2.DisplayResults();
            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));


            // OOP Lab 1 Problem 7
            ChangeInCoins change1 = new ChangeInCoins();

            change1.change = 0.92;

            Console.ReadLine();
            Console.WriteLine("\nOOP | Laboratory 1 | Chapter 2 | Exercise 7");
            change1.DisplayResults();
            Console.WriteLine("Time Stamp\t\t: " + timeStamp.ToString("F"));

            // new values
            ChangeInCoins change2 = new ChangeInCoins();

            change2.change = 0.27;

            Console.WriteLine("");
            change2.DisplayResults();
            Console.WriteLine("Time Stamp\t\t: " + timeStamp.ToString("F"));


            // OOP Lab 1 Problem 8
            ComputeWeightedAverage weightedAverage1 = new ComputeWeightedAverage();

            weightedAverage1.homework = 97;
            weightedAverage1.projects = 82;
            weightedAverage1.quizzes = 60;
            weightedAverage1.exams = 75;
            weightedAverage1.finalExam = 80;

            Console.ReadLine();
            Console.WriteLine("\nOOP | Laboratory 1 | Chapter 2 | Exercise 8");
            weightedAverage1.DisplayResults();
            Console.WriteLine("Time Stamp\t\t: " + timeStamp.ToString("F"));

            // new object
            ComputeWeightedAverage weightedAverage2 = new ComputeWeightedAverage();

            weightedAverage2.homework = 87;
            weightedAverage2.projects = 85;
            weightedAverage2.quizzes = 70;
            weightedAverage2.exams = 90;
            weightedAverage2.finalExam = 95;

            Console.WriteLine("");
            weightedAverage2.DisplayResults();
            Console.WriteLine("Time Stamp\t\t: " + timeStamp.ToString("F"));


            // OOP Lab 1 Problem 9
            ComputeMoneyToReceive moneyToReceive1 = new ComputeMoneyToReceive();

            moneyToReceive1.amountOfCasesSold = 29;
            moneyToReceive1.amountOfBarsInEachCase = 100;
            moneyToReceive1.percentRequiredToGive = 0.10;

            Console.ReadLine();
            Console.WriteLine("\nOOP | Laboratory 1 | Chapter 2 | Exercise 9");
            moneyToReceive1.DisplayResults();
            Console.WriteLine("Time Stamp\t\t\t: " + timeStamp.ToString("F"));


            // OOP Lab 1 Problem 10
            ConvertToPricePerPound pricePerPound1 = new ConvertToPricePerPound();

            pricePerPound1.brandOfMeat = "Montreal Smoked Meat";
            pricePerPound1.pricePerIndicatedGram = 2.09;
            pricePerPound1.indicatedGrams = 100;

            Console.ReadLine();
            Console.WriteLine("\nOOP | Laboratory 1 | Chapter 2 | Exercise 10");
            pricePerPound1.DisplayResults();
            Console.WriteLine("Time Stamp\t: " + timeStamp.ToString("F"));
        }
    }
}
