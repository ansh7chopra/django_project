document.addEventListener("DOMContentLoaded", function () {
    var today = new Date();
    var minDate = formatDate(today);

    document.getElementById("dateInput").value = minDate;

    var nextWeek = new Date();
    nextWeek.setDate(today.getDate() + 7);
    var maxDate = formatDate(nextWeek);

    document.getElementById("dateInput").setAttribute("max", maxDate);
    document.getElementById("dateInput").setAttribute("min", minDate);
});

function formatDate(date) {
    var year = date.getFullYear();
    var month = (date.getMonth() + 1).toString().padStart(2, "0");
    var day = date.getDate().toString().padStart(2, "0");
    return year + "-" + month + "-" + day;
}

document.querySelectorAll('.pvr-link').forEach(function (link) {
    link.addEventListener('click', function (event) {
        event.preventDefault();
        var pvrName = this.getAttribute('data-pvr');
        var showTime = this.getAttribute('data-show');
        var selectedDate = document.getElementById('dateInput').value;
        localStorage.setItem('selectedPVR', pvrName);
        localStorage.setItem('selectedShowTime', showTime);
        localStorage.setItem('selectedDate', selectedDate);
        console.log('Selected PVR:', pvrName);
        console.log('Selected Show Time:', showTime);
        console.log('Selected Date:', selectedDate);

        window.location.href = '/seat_selection/'
    });
});