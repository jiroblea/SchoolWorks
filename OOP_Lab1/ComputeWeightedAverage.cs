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
        const double WEIGHT_OF_HOMEWORK = 0.10;
        const double WEIGHT_OF_PROJECTS = 0.35;
        const double WEIGHT_OF_QUIZZES = 0.10;
        const double WEIGHT_OF_EXAMS = 0.30;
        const double WEIGHT_OF_FINAL_EXAM = 0.15;

        public double WeightedScores()
        {
            double weightedScores = (homework * WEIGHT_OF_HOMEWORK) + (projects * WEIGHT_OF_PROJECTS) + (quizzes * WEIGHT_OF_QUIZZES) + (exams * WEIGHT_OF_EXAMS) + (finalExam * WEIGHT_OF_FINAL_EXAM);
            return weightedScores;
        }

        public double TotalWeight()
        {
            double totalWeight = Math.Round(WEIGHT_OF_HOMEWORK + WEIGHT_OF_PROJECTS + WEIGHT_OF_QUIZZES + WEIGHT_OF_EXAMS + WEIGHT_OF_FINAL_EXAM);
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
            Console.WriteLine("Weighted Average\t: " + WeightedAverage());
        }
    }
}
