const totalScore = [];

function drawDice(){
    const number = Math.floor(Math.random() * 6) + 1;
    let dice = document.getElementById('dice');
    let numberText = document.querySelector("#diceContainer > h1");

    dice.src = `img/${number}.png`;
    numberText.textContent = number;
    console.log(number);

    totalScore.push(number);
    drawAverageScore(totalScore);
    fillTable(number);
}

function fillTable(value) {
    if(document.getElementById('diceTable').getAttribute('visible') === 'false') {
        document.getElementById('diceTable').setAttribute('visible', 'true');
    }
    document.getElementById(`score${value}`).textContent = parseInt(document.getElementById(`score${value}`).textContent) + 1;
}

function drawAverageScore(total) {
    const result = document.querySelector('#diceTable p');
    const sum = total.reduce((a, b) => a + b, 0);
    const avg = (sum / total.length).toFixed(2) || 0;

    result.textContent = `Het totaal is: ${sum} | Het gemiddelde: ${avg}.`;
}