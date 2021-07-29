using System;
using System.Collections.Generic;
using System.Text;

namespace OOP_Lab1
{
    class ComputeWeightedAverage
    {
        // variables
        public int homework;
        public int projects;
        public int quizzes;
        public int exams;
        public int finalExam;

        // weights
        const double WEIGHTOFHOMEWORK = 0.10;
        const double WEIGHTOFPROJECTS = 0.35;
        const double WEIGHTOFQUIZZES = 0.10;
        const double WEIGHTOFEXAMS = 0.30;
        const double WEIGHTOFFINALEXAM = 0.15;

        public double WeightedScores()
        {
            double weightedScores = (homework * WEIGHTOFHOMEWORK) + (projects * WEIGHTOFPROJECTS) + (quizzes * WEIGHTOFPROJECTS) + (exams * WEIGHTOFEXAMS) + (finalExam * WEIGHTOFFINALEXAM);
            return weightedScores;
        }

        public double TotalWeight()
        {
            double totalWeight = Math.Round(WEIGHTOFHOMEWORK + WEIGHTOFPROJECTS + WEIGHTOFQUIZZES + WEIGHTOFEXAMS + WEIGHTOFFINALEXAM);
            return totalWeight;
        }

        public double WeightedAverage()
        {
            double weightedAverage = Math.Round(WeightedScores() / TotalWeight(), 2);
            return weightedAverage;
        }

        public void DisplayResults()
        {
            Console.WriteLine("Homework\t\t: " + homework);
            Console.WriteLine("Projects\t\t: " + projects);
            Console.WriteLine("Quizzes\t\t\t: " + quizzes);
            Console.WriteLine("Exams\t\t\t: " + exams);
            Console.WriteLine("Final Exam\t\t: " + finalExam);
            Console.WriteLine("Weigthed Average\t: " + WeightedAverage());
        }
    }
}
