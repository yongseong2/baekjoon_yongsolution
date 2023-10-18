function solution(s) {
    const list = s.split(' ').map(Number)
    let maxNum = Math.max(...list)
    let minNum = Math.min(...list)
    const answer = [minNum, maxNum].join(' ')
    
    
    return answer
}