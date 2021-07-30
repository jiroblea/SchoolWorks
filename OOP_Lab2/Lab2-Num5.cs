
///LAB 2 NUM 5
using System;

public class MainClass
{
    public static void Main(String[] args)
    {
        double temperature;
        double computation;
        
        temperature = GetTemperature("Fahrenheit");
        computation = CalculateCelsius(temperature);
        DisplayResult(temperature, "Fahrenheit", computation, "Celsius");
    }

    private static double GetTemperature(string label)
    {
        string input;
        double temperature;

        Console.WriteLine("Enter " + label + " temperature:");
        input = Console.ReadLine();
        temperature = Convert.ToDouble(input);

        return temperature;
    }

    private static double CalculateCelsius(double fahrenheit)
    {
        double celsius;
        
        celsius = (fahrenheit - 32) * 5 / 9;
        
        return celsius;
    }

    private static void DisplayResult(double fahrenheit, string fromLabel, double celsius, string toLabel)
    {
        Console.WriteLine(fahrenheit.ToString() + "° " + fromLabel + " is the original value, and is converted to " + celsius.ToString() + "° " + toLabel);
    }
}