// 函数定义
function func1(){
    console.log(123)
}
func1()

// 带参数的函数
function func2(a, b){
    console.log(arguments);
    console.log(arguments.length)
    console.log(a, b);
}
func2(1, 2)

// 函数返回值
function func3(a, b){
    return a + b;
}

func3(3, -1);

// 匿名函数
// 方式一：声明变量并接收匿名函数
var ret = function(a, b) {
    return a + b;
}

ret(3, 10)

// 方式二：页面加载时立即执行的匿名函数(函数在声明后不需要对象接收，执行调用)
    (function(a, b) {
        return a + b;
    })(10, 20)

// 闭包
var city = '北京';
function func(){
    var city = '上海';
    function inner(){
        console.log(city);
    }
    return inner;
}

var ret = func()
ret()

// 面向对象
function Person(name) {
    this.name = name;
}
// 添加成员方法
Person.prototype.sum = function(a, b){return a + b;}

// 类的实例化
var alex = new Person('alex');

// 访问类中的成员
console.log(alex.name);
var ret = alex.sum(10, 20);
console.log(ret);