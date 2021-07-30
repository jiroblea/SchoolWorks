// written by jeron
using System;

public class Main2Class
{
    public static void Main(String[] args)
    {
        double meters;
        double inches;
        double NewInches;
        int feet;

        
            meters = GetMeters("Meters");
            inches = CalculateInches(meters);
            NewInches = CalculateNewInches(inches); // variables in camelCase
            feet = CalculateFeet(inches);
            DisplayResult(meters, feet, NewInches);
    }

    private static double GetMeters(string label)
    {
        string input;
        double meters;

        Console.WriteLine("Enter meters:");
        input = Console.ReadLine();
        meters = Convert.ToDouble(input);

        return meters;
    }

    private static double CalculateInches(double meters)
    {
        double inches;
        
        inches = meters * 39.37;
        
        return inches;
    }

    private static int CalculateFeet(double inches)
    {
        int feet;

        feet = (int)inches / 12;

        return feet; 
    }

    private static int CalculateNewInches(double inches)
    {
        int NewInches;

        NewInches = (int)inches % 12;

        return NewInches;
    }

    private static void DisplayResult(double meters, double feet, double NewInches)
    {
        Console.WriteLine(meters.ToString() + " meters is the original value, and is converted to " + feet.ToString() + " feet and " + NewInches.ToString() + " inches");
    }
}