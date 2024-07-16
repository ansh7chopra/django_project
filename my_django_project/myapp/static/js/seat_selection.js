document.addEventListener("DOMContentLoaded", function () {
    let seats = document.querySelector(".all-seats");
    let selectedSeats = JSON.parse(localStorage.getItem("selectedSeats")) || [];

    function generateSeats(availableSeats) {
        seats.innerHTML = ""; 
        for (let i = 0; i < availableSeats; i++) {
            seats.insertAdjacentHTML(
                "beforeend",
                `<input type="checkbox" name="tickets" id="s${i + 1}" />
                <label for="s${i + 1}" class="seat available">${i + 1}</label>`
            );
        }
    }
    
    const availableSeats = 60;

    generateSeats(availableSeats);

    selectedSeats.forEach(seatId => {
        const seatCheckbox = document.getElementById(seatId);
        if (seatCheckbox) {
            seatCheckbox.checked = true;
            seatCheckbox.disabled = true; 
            seatCheckbox.nextElementSibling.classList.remove('available');
            seatCheckbox.nextElementSibling.classList.add('booked');
        }
    });

    let tickets = seats.querySelectorAll("input");
    tickets.forEach((ticket) => {
        ticket.addEventListener("change", () => {
            let amount = document.querySelector(".amount").innerHTML;
            let count = document.querySelector(".count").innerHTML;
            amount = Number(amount);
            count = Number(count);

            if (ticket.checked) {
                selectedSeats.push(ticket.id);
                count += 1;
                amount += 200;
            } else {
                selectedSeats = selectedSeats.filter((seat) => seat !== ticket.id);
                count -= 1;
                amount -= 200;
            }
            document.querySelector(".amount").innerHTML = amount;
            document.querySelector(".count").innerHTML = count;

            if (count > 0) {
                paybtn.style.display = "block";
            } else {
                paybtn.style.display = "none";
            }

            localStorage.setItem("selectedSeats", JSON.stringify(selectedSeats));
            console.log("Selected seats:", selectedSeats);
        });
    });

    document.getElementById("paybtn").addEventListener("click", function () {

        window.location.href = "/payment_page/";
    });
});



