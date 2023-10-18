function solution(s) {
    let countTransformations = 0;
    let countZeros = 0;

    while (s !== "1") {
        // 0의 개수 세기
        const zeros = [...s].filter(char => char === '0').length;
        countZeros += zeros;

        // 0을 제거하고 남은 1의 개수를 이진법으로 변환
        s = (s.length - zeros).toString(2);
        
        countTransformations++;
    }

    return [countTransformations, countZeros];
}
