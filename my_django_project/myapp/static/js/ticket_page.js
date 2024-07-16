window.onload = function() {
    // Retrieve booking information from local storage
    const selectedMovie = localStorage.getItem("selectedMovie");
    const selectedPVR = localStorage.getItem("selectedPVR");
    const selectedShowTime = localStorage.getItem("selectedShowTime");
    const selectedDate = localStorage.getItem("selectedDate");
    const selectedSeats = JSON.parse(localStorage.getItem("selectedSeats"));

    // Display the booking information on the ticket page
    document.getElementById("movieName").innerText = selectedMovie;
    document.getElementById("pvrName").innerText = selectedPVR;
    document.getElementById("showtime").innerText = selectedShowTime;
    document.getElementById("date").innerText = selectedDate;
    document.getElementById("selectedSeats").innerText = selectedSeats.join(", ");

    // Logging retrieved values to console for verification
    console.log("Booking information retrieved from local storage:");
    console.log("Selected Movie:", selectedMovie);
    console.log("Selected PVR:", selectedPVR);
    console.log("Selected Show Time:", selectedShowTime);
    console.log("Selected Date:", selectedDate);
    console.log("Selected Seats:", selectedSeats);


    // Prepare booking data object
    const bookingData = {
        movie: selectedMovie,
        pvr: selectedPVR,
        showTime: selectedShowTime,
        date: selectedDate,
        seats: selectedSeats
    };

    // Send the booking information to the server using fetch API
    fetch('/save_booking/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token if CSRF protection is enabled
        },
        body: JSON.stringify(bookingData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Booking data sent to server:', data);
        } else {
            console.error('Error saving booking data:', data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
};

// Function to get CSRF token from cookies (if CSRF protection is enabled)
function getCookie(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}