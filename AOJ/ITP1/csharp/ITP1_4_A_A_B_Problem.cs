using System;

class P
{
    static void Main()
    {
        var a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        Console.WriteLine($"{a[0] / a[1]} {a[0] % a[1]} {1.0 * a[0] / a[1] :f5}");
    }
}
