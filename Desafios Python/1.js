function fatorial(num){
    res = num
    for(let i = 1;i < num;i++){
        res *= i
    }
    return res
}
console.log(fatorial(5))