using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab1
{
    class ComputeAverageScore
    {
        const int AMOUNTOFSCORE = 5;
        public int score1;
        public int score2;
        public int score3;
        public int score4;
        public int score5;

        public double Average()
        {
            double average = (score1 + score2 + score3 + score4 + score5) / AMOUNTOFSCORE;
            double roundedAverage = Math.Ceiling(average);
            return roundedAverage;
        }

        public void DisplayResults()
        {
            Console.WriteLine("Five Scores\t: " + score1 + ", " + score2 + ", " + score3 + ", " + score4 + ", " + score5);
            Console.WriteLine("Average\t\t: " + Average());
        }
    }
}
