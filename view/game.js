document.addEventListener("DOMContentLoaded", function () {
    let startTime;
    let score = 0;
    let flipsElement = document.querySelector(".flips span");
    let timeElement = document.querySelector(".time span");
    let username;

    fetch('/api/user')
        .then(response => response.json())
        .then(data => {
            if (data.username) {
                username = data.username;
                document.querySelector(".name span").innerHTML = username;
            } else {
                username = null;
                document.querySelector(".name span").innerHTML = "Unknown";
            }
        })
        .catch(error => {
            console.error('Error fetching username:', error);
            document.querySelector(".name span").innerHTML = "Unknown";
        });

    document.querySelector(".buttons span").onclick = function () {
        // if (!username) {
           // alert("Please log in first.");
           // return;
        //}
        document.querySelector(".buttons").remove();
        startTime = Date.now();  // Set the start time here
        timeElement.innerHTML = '00:00';  // Reset time display
        gameInterval = setInterval(updateTime, 1000);
        gameBlocks.style.visibility = 'visible';  // Show game blocks
    };


let duration = 500;

let gameBlocks = document.querySelector(".game-blocks");
gameBlocks.style.visibility = 'hidden';  // Hide game blocks initially


let cards = Array.from(gameBlocks.children);

let cardsOrder = [...Array(cards.length).keys()];

console.log(cardsOrder);
cardsShuffle(cardsOrder);
console.log(cardsOrder);

// order css property to cards
cards.forEach((card, index) => {
    card.style.order = cardsOrder[index];

    // click event
    card.addEventListener("click", function () {
        cardsFlip(card);
    });
});


// flipping cards
function cardsFlip(clickedCard) {
    // add class "is-clicked"
    clickedCard.classList.add("is-clicked");

    // all clicked cards
    let clickedCards = cards.filter(clickedCard => clickedCard.classList.contains("is-clicked"));
    // two flipped cards
    if (clickedCards.length === 2) {
        // unable to click another card
        noClick();

        // check if two cards are same
        matchedCards(clickedCards[0], clickedCards[1]);
    }
}

// stop clicking other cards
function noClick() {
    // add class no-click on game-blocks container
    gameBlocks.classList.add("no-click");
    // remove class no-click after 1 second
    setTimeout(() => {
        gameBlocks.classList.remove("no-click");
    }, duration);
}

// matching cards
function matchedCards(firstCard, secondCard) {

    if (firstCard.getAttribute("harry-potter") === secondCard.getAttribute("harry-potter")) {
        firstCard.classList.remove("is-clicked");
        secondCard.classList.remove("is-clicked");

        firstCard.classList.add("is-matched");
        secondCard.classList.add("is-matched");

        document.getElementById("matched").play();

        score += 10;

        if (document.querySelectorAll('.is-matched').length === cards.length) {
            clearInterval(gameInterval);  // Stop the timer
            let timeTaken = Math.floor((Date.now() - startTime) / 1000);
            let finalScore = score - (parseInt(flipsElement.innerHTML) * 5);
            alert(`Game Over! Your score is ${finalScore}. Time taken: ${timeTaken} seconds.`);
            submitScore(finalScore);
        }

    } else {
        flipsElement.innerHTML = parseInt(flipsElement.innerHTML) + 1;
        setTimeout(() => {
            firstCard.classList.remove("is-clicked");
            secondCard.classList.remove("is-clicked");
        }, duration);

        document.getElementById("wrong").play();
    }
}

function updateTime() {
    let elapsedTime = Math.floor((Date.now() - startTime) / 1000);
    let minutes = Math.floor(elapsedTime / 60).toString().padStart(2, '0');
    let seconds = (elapsedTime % 60).toString().padStart(2, '0');
    timeElement.innerHTML = `${minutes}:${seconds}`;
}

//send score to user's scores
function submitScore(finalScore) {
    fetch('/api/score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ score: finalScore }),
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error submitting score:', error);
        });
}

// shuffling cards
function cardsShuffle(array) {
    let currentIndex = array.length;
    let randomIndex;
    let temp;

    while (currentIndex > 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // save current number in temp
        temp = array[currentIndex];
        // current element = random
        array[currentIndex] = array[randomIndex];
        // random = get the number in temp
        array[randomIndex] = temp;
    };
    return array;
    }
});
