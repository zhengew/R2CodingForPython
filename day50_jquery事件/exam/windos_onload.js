<!-- 测试原生js的 window.onload页面载入事件的覆盖问题  -->

// window.onload = function (){
//     var c1 = document.getElementsByClassName('c1')[0];
//     c1.style.backgroundColor = 'green';
// }

<!-- 测试jquery方式实现页面载入事件，避免覆盖现象 -->
$(function(){
    $('.c1').css({'background-color': 'orange', 'width': '300px', 'height': '300px'})
})