// gcd(a, b)を返す
// ax + by = gcd(a, b)となるようにx, yを書き換える
#include<stdio.h>
int x;
int y;
int extgcd(int a, int b, int& x, int& y) {
    // printf("%d\n", x);
    printf("1term\n");
    printf("%d\n", x);
    printf("%d\n", y);

    if (a < b) return extgcd(b, a, y, x);
    // xとyを入れ替え忘れないように注意
    
    if (b > 0) {
        int g = extgcd(b, a % b, y, x);
        y -= (a / b) * x;
        // printf("1term\n");
        // printf("%d\n", a);
        // printf("%d\n", b);
        // printf("%d\n", x);
        // printf("%d\n", y);
        return g;
    } else {
        x = 1, y = 0;
        printf("aaaaaa");
        return a;
    }
}

int main(void){
    extgcd(11,4,x,y);
    // printf("%d\n",x);
}