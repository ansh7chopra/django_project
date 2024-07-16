document.addEventListener('DOMContentLoaded', function() {
    // Parse the query parameters to extract movie name and ticket data
    const urlParams = new URLSearchParams(window.location.search);
    const movieName = urlParams.get('movie');
    const ticketDataJson = urlParams.get('data');
    const ticketData = JSON.parse(ticketDataJson);

    // Display ticket details in the HTML page
    const ticketDetailsContainer = document.getElementById('ticketDetailsContainer');
    if (ticketDetailsContainer) {
        const list = document.createElement('ol');
        ticketData.forEach(ticket => {
            const listItem = document.createElement('li');
            listItem.innerHTML = ` <span class="bold">Movie Name:</span> ${ticket.movie}, <span class="bold">PVR:</span> ${ticket.pvr}, <span class="bold">Date:</span> ${ticket.date}, <span class="bold">Show Time:</span> ${ticket.show_time}, <span class="bold">Seats:</span> ${ticket.seats}`;
            list.appendChild(listItem);
        });
        ticketDetailsContainer.appendChild(list);
    } else {
        console.error('ticketDetailsContainer element not found');
    }

    // Add event listener to the download button
    const downloadBtn = document.getElementById('downloadBtn');
    downloadBtn.addEventListener('click', function() {
        downloadExcel(ticketData, movieName);
    });
});

function downloadExcel(data, movieName) {
    // Convert the data to a worksheet
    const ws = XLSX.utils.json_to_sheet(data);

    // Create a new workbook and append the worksheet
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Ticket Sales');

    // Generate a file name
    const filename = `${movieName}_ticket_sales.xlsx`;

    // Write the workbook to a file and trigger the download
    XLSX.writeFile(wb, filename);
}
