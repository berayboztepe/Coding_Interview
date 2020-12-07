using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;


namespace Project_Euler_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Func<int> q1 = () =>
            {
                int sum = 0;
                for (int i = 0; i < 1000; i++)
                {
                    if (i % 3 == 0 || i % 5 == 0)
                    {
                        sum += i;
                    }
                }
                return sum;
            };
            Console.WriteLine("Soru 1 = " + q1());
            Console.WriteLine("Soru 2 = " + q2());
            Console.WriteLine("Soru 3 = " + q3());
            Console.WriteLine("Soru 4 = " + Q4());
            Console.WriteLine("Soru 5 = " + q5());
            Console.WriteLine("Soru 6 = " + q6());
            Console.WriteLine("Soru 7 = " + q7());
            Console.WriteLine("Soru 8 = " + q8());
            Console.WriteLine("Soru 9 = " + q9());
            Console.WriteLine("Soru 10 = " + q10());





        }
        static int q2()
        {
            int fib1 = 1;
            int fib2 = 2;
            int sum = 0;
            sum += fib2;
            while (true)
            {
                int fib = fib1 + fib2;
                if (fib > 4000000) break;
                else if (fib % 2 == 0)
                {
                    sum += fib;
                }
                fib1 = fib2;
                fib2 = fib;
            }
            return sum;
        }
        static int q3()
        {
            Func<int, bool> check_prime = (x) =>
            {
                for (int i = 2; i < Math.Sqrt(x) + 2; i++)
                {
                    if (x % i == 0) return false;

                }
                return true;
            };
            long n = 600851475143;
            List<int> numbers = new List<int>();
            for (int i = 2; i < Math.Sqrt(n) + 1; i++)
            {
                if (n % i == 0)
                {
                    if (check_prime(i) == true) numbers.Add(i);
                }
            }
            int max = numbers.Max();
            return max;
        }

        static int Q4()
        {
            int pal = 0;
         

            
            for (int a = 100; a < 1000; a++)
            {

                for (int b = 100; b < 1000; b++)
                {
                    int sonuc = a * b;
                    char[] sonuc1 = sonuc.ToString().ToCharArray();
                    int control = 0;
                    for (int i = 0; i < sonuc1.Length; i++)
                    {
                        if (sonuc1.ToArray()[i] == sonuc1.Reverse().ToArray()[i]) continue;
                        else
                        {
                            control = 1;
                            break;
                        }
                    }
                    if(control == 0)
                    {
                        if (sonuc > pal) pal = sonuc;
                    }

                }
            }
            return pal;
        }
        static int q5()
        {
            var n = 2520;
            while (true)
            {
                int control = 1;
                for(int i = 2; i < 21; i++)
                {
                    if (n % i != 0) 
                    {
                        control = 0;
                        break;
                    }
                }
                if(control == 1)
                {
                    break; 
                }
                n += 10;
            }
            return n;
        }
        static double q6()
        {
            double sum = 0;
            double sum1 = 0;
            for(int i = 1; i<101; i++)
            {
                sum += i;
                sum1 += Math.Pow(i, 2);
            }
            return Math.Abs(Math.Pow(sum, 2) - sum1);
        }
        static int q7()
        {
            int n = 3;
            int counter = 1;
            Func<int, bool> check_prime = (x) =>
            {
                for (int i = 2; i < Math.Sqrt(x) + 1; i++)
                {
                    if (x % i == 0) return false;

                }
                return true;
            };
            while (true)
            {
                if (check_prime(n)) counter++;
                if (counter == 10001) break;
                n += 2;
            }
            return n;
        }
        static long q8()
        {
            long max = 0;
            String a = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";
            
            for(int i = 0; i<a.Length-13; i++)
            {
                long sonuc = 1;
                for (int j = 0; j<13; j++)
                {
                    sonuc *= int.Parse(a.Substring(i + j, 1));
                }
                if (sonuc > max)
                {
                    max = sonuc;
                }
            }
            return max;
        }

        static int q9()
        {
            for(int a = 1; a<500; a++)
            {
                for(int b = a; b<500; b++)
                {
                    double c = Math.Sqrt(Math.Pow(a, 2) + Math.Pow(b, 2));
                    if(c == Convert.ToInt32(c))
                    {
                        if (a + b + c == 1000) return a * b * Convert.ToInt32(c);
                    }
                }
            }
            return 0;
        }
        static long q10()
        {
            Func<int, bool> check_prime = (x) =>
            {
                for (int i = 2; i < Math.Sqrt(x) + 1; i++)
                {
                    if (x % i == 0) return false;

                }
                return true;
            };
            long sum = 2;
            for(int n = 3; n<2000000; n += 2)
            {
                if (check_prime(n)) sum += n;
            }
            return sum;
        }

    }
}

