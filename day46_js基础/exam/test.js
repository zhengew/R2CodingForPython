var a = 1;
switch (a) {
    case 1:
        alert('a===1')
        break;
    case 2:
        alert('a===2')
        break;
    default:
        alert('a === 3')
}

// for 循环
var arr = [1, 2, 3, 4, 5]
// 方式一
for (var i in arr){
    console.log(i, arr[i])
}

// 方式二
for (var i = 0; i < arr.length; i++){
    console.log(i, arr[i])
}

// while循环
var i = 5;
while (i > 0){
    console.log(i);
    i--;
}
