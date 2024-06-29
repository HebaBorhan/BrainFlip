document.querySelector(".buttons span").onclick = function () {
    let UserName = prompt("Please Enter Your Name");

    if (UserName == null || UserName == "") {
        document.querySelector(".name span").innerHTML = "Unknown";
    } else {
        document.querySelector(".name span").innerHTML = UserName;
    }

    document.querySelector(".buttons").remove();
};

let duration = 2000;

let gameBlocks = document.querySelector(".game-blocks");

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
    let flipsElement = document.querySelector(".flips span");

    if (firstCard.getAttribute("harry-potter") === secondCard.getAttribute("harry-potter")) {
        firstCard.classList.remove("is-clicked");
        secondCard.classList.remove("is-clicked");

        firstCard.classList.add("is-matched");
        secondCard.classList.add("is-matched");

        document.getElementById("matched").play();

    } else {
        flipsElement.innerHTML = parseInt(flipsElement.innerHTML) + 1;
        setTimeout(() => {
            firstCard.classList.remove("is-clicked");
            secondCard.classList.remove("is-clicked");
        }, duration);

        document.getElementById("wrong").play();
    }
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
};
