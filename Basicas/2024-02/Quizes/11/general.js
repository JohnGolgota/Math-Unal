function general(a,b,c){
    let sqrt = Math.sqrt(b**2-4*a*c);
    let x1 = (-b+sqrt)/(2*a);
    let x2 = (-b-sqrt)/(2*a);
    return [x1,x2];
}