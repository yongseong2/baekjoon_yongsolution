function solution(s) {
    let answer = ''
    let isNewWord = true
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' ') {
            answer += s[i]
            isNewWord = true
        } 
        else if (isNewWord) {
            answer += s[i].toUpperCase()
            isNewWord = false
        }
        else  {
            answer += s[i].toLowerCase()
        }
    }
    return answer
}