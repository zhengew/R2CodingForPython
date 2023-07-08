/* 测试 STATICFILES_DIRS 静态文件配置 */

var username = document.getElementById('username')

username.onfocus = function func(){
    this.style.backgroundColor = 'lightgray';
}

username.onblur = function func(){
    this.style.backgroundColor = 'white';
}
