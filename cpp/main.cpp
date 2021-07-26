
typedef struct Base1 {
    int v1;
//    private:   //error!
    int v3;
public:     //显示声明public
    int v2;
    void print(){
        printf("%s\n","hello world");
    };
}B;
void B() {}  //error! 符号 "B" 已经被定义为一个 "struct Base1" 的别名


