from math import sqrt
'''
function solve_equation(int $a = 1, int $b = 1, int $c = 1): array
{
    $d = $b ** 2 - 4 * $a * $c;
    if ($d <= 0)
    {
        return ($d == 0 and $a != 0) ? [ -$b / 2 * $a ] : [];
    }
    else
    {
        $d_root = sqrt($d);
        $t = 2 * $a;
        return [ (-$b + $d_root) / $t, (-$b - $d_root) / $t ];
    }
}

var_dump( solve_equation(4, -6, 0) );

'''


def solve_equation(a: int = 1, b: int = 1, c: int = 1):
    d = b ** 2 - 4 * a * c
    if d <= 0:
        if d == 0 and a != 0:
            return -b / 2 * a
        else:
            return False
    else:
        d_root = sqrt(d)
        double_a = 2 * a
        return [ 
            (-b + d_root) / double_a,
            (-b - d_root) / double_a 
        ]