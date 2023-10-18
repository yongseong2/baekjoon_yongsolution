function solution(A,B){
    let answer = 0;

    const sortedA = A.sort((a, b) => a - b); // 오름차순 정렬
    const sortedB = B.sort((a, b) => b - a); // 내림차순 정렬
    
    for (let i = 0; i < A.length; i++) {
        answer += sortedA[i] * sortedB[i];
    }

    return answer;
}
