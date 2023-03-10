var like = document.getElementById('like');
var dislike = document.getElementById('dislike');
var num1 = document.getElementById('num1');
var num2 = document.getElementById('num2');
var flag1 = 0;
var flag2 = 0;
like.onclick = function () {
    if (flag1 === 0) {
        num1.innerHTML++;
    }
    if (flag1 === 1) {
        num1.innerHTML--;
    }
    if (flag1 === 2) {
        num1.innerHTML++;
        flag1 = 0;
    }
    flag1++;
}
dislike.onclick = function () {
    if (flag2 === 0) {
        num2.innerHTML++;
    }
    if (flag2 === 1) {
        num2.innerHTML--;
    }
    if (flag2 === 2) {
        num2.innerHTML++;
        flag2 = 0;
    }
    flag2++;
}